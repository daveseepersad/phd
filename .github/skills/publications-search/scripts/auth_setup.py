# /// script
# requires-python = ">=3.12"
# dependencies = ["playwright>=1.47"]
# ///
"""One-time interactive login that persists an institutional session.

Opens a headed Chromium against a dedicated profile directory, waits while you
sign in through your library's SSO, then leaves the cookies on disk so the
other scripts can run unattended.

Windows Edge profiles cannot be reused directly: Chromium encrypts cookies with
the Windows DPAPI user key, which is unavailable under WSL. This dedicated
profile is the portable equivalent.
"""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import (
    DEFAULT_PROFILE_DIR,
    check_access,
    launch_context,
    save_storage_state,
    seed_library_access,
)
from playwright.sync_api import sync_playwright

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

logger = logging.getLogger(__name__)

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--profile-dir",
        type=Path,
        default=DEFAULT_PROFILE_DIR,
        help="Persistent browser profile directory.",
    )
    parser.add_argument(
        "--start-url",
        default="https://sherman.library.nova.edu/account",
        help="Library page to open first for SSO sign-in.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Skip the interactive wait and only report current access status.",
    )
    return parser


def report_access(context) -> bool:
    return all(check_access(context, log=logger).values())


def main() -> int:
    args = create_parser().parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    args.profile_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        # Always headed: ACM's challenge and Scholar both reject headless Chromium.
        context = launch_context(p, args.profile_dir, headless=False)
        if args.check:
            seed_library_access(context, log=logger)
            ok = report_access(context)
            save_storage_state(context, args.profile_dir)
            context.close()
            return EXIT_SUCCESS if ok else EXIT_FAILURE

        page = context.pages[0] if context.pages else context.new_page()
        page.goto(args.start_url, wait_until="domcontentloaded")
        logger.info("Sign in through the browser window, including any MFA prompt.")
        logger.info("Visit dl.acm.org and ieeexplore.ieee.org once to seed both sessions.")
        logger.info("Press Enter here when finished...")
        try:
            input()
        except (EOFError, KeyboardInterrupt):
            logger.warning("Interrupted before confirmation.")
            context.close()
            return 130

        seed_library_access(context, log=logger)
        ok = report_access(context)
        state_path = save_storage_state(context, args.profile_dir)
        context.close()
        logger.info("Profile saved to %s", args.profile_dir)
        logger.info("Session state saved to %s", state_path)
        if not ok:
            logger.warning("At least one database did not look authenticated.")
        return EXIT_SUCCESS if ok else EXIT_FAILURE


if __name__ == "__main__":
    sys.exit(main())
