# keep-awake-win

A small, transparent utility that requests Windows **not** to enter idle sleep using the Win32 `SetThreadExecutionState` API. Intended for **personal or team** use on machines you control (presentations, long-running computations, media playback).
**This project does not simulate user input and must not be used to evade monitoring or logging.**

---

## Features

* Uses the documented Win32 API (no simulated keystrokes or mouse movement)
* Lightweight: single Python file, no external dependencies
* Simple heartbeat output so you know it’s running
* Optional *away-mode* flag for media-server scenarios

---

## Requirements

* Windows OS
* Python 3.7 or newer

---

## Installation

1. Clone or download this repo.
2. (Optional) Create a virtual environment:

   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```
3. No additional packages required.

---

## Usage

```bash
# default: heartbeat every 60 seconds
python keep_awake_win.py

# set heartbeat interval to 30 seconds
python keep_awake_win.py -i 30

# enable away mode (for media server / away-mode scenarios)
python keep_awake_win.py -a
```

Press `Ctrl+C` to stop. The script restores normal sleep behavior on exit.

---

## Example output

```
Keeping system awake using SetThreadExecutionState. Press Ctrl+C to stop.
[12:34:56] Awake request active. Sleeping 60s.
[12:35:56] Awake request active. Sleeping 60s.
...
Stopping and restoring normal sleep behavior...
```

---

## Important notes / acceptable use

* **Do not** use this tool to evade workplace monitoring, logging, or security controls.
* Only run this on machines you own or have explicit permission to modify.
* Follow your organization’s acceptable-use policies and local laws.
* The author is not responsible for misuse.

---

## Troubleshooting

* **“SetThreadExecutionState failed”** — rare; try running Python as Administrator. Verify you are on Windows.
* If the system still sleeps: double-check power plan settings in Windows (`Control Panel → Power Options`) and that no group policy or management tool forces sleep behavior.

---

## Contributing

Contributions are welcome for bug fixes, documentation improvements, or small quality-of-life features. Please:

1. Fork the repo
2. Create a branch: `git checkout -b fix/your-change`
3. Commit your changes: `git commit -m "Describe change"`
4. Open a pull request with a clear description of the change

Keep contributions aligned with the project goal: honest, transparent keep-awake behavior.

---

## License

MIT License — replace `<Your Name>` and the year in `LICENSE` file.

---

## Contact

For questions or feedback, open an issue in the repository or contact the maintainer (replace with your email or GitHub handle).

---

If you want, I can:

* Produce the `README.md` file as a downloadable file,
* Add badges (build / python version / license),
* Or create a short `CONTRIBUTING.md` to go with it. Which would you like?
