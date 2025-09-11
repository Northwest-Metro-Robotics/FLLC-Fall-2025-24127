# FLL Pybricks Starter

A batteries-included starter kit for FIRST® LEGO® League Challenge teams using **Pybricks** on SPIKE Prime / Robot Inventor.

**Highlights**
- Safe hardware abstraction (drivebase, sensors, attachments)
- Gyro calibration, mission runner menu, and E‑stop
- P & PD line following, PID turn, straight drives
- Configurable robot profiles (ports, wheelbase, etc.)
- Docs & lesson plans

> Generated 2025-09-02. MIT-licensed.

## Prerequisites
* Download and install [Git for Windows](https://git-scm.com/downloads/win)

## Quick start
1. Flash your hub with the latest **Pybricks** firmware.
2. Open `src/` as your project in Pybricks Code.
3. Rename `.vscode.example` to `.vscode` (delete existing .vscode folder if needed)
4. Run `src/main.py`. Use Left/Right to choose a mission, Center to run, Back to stop.

## Layout
```
src/
  core/         # HAL: drive, sensors, pid, safety, gyro
  missions/     # Mission runner + example missions
  utils/        # Logger, math, tuning helpers
  config/       # ports.json and robot profiles
```
