# keysight_p9375a

============

A quick PyMeasure Instrument Class for the Keysight P9375A

---

Todo List

- [x] Create P9375A boilerplate
- [x] Create Channels class
- [ ] Create Traces class ?
- [x] Create uv project
- [x] Create venv `uv venv .venv`
- [x] Add pyvisa, pyvisa-py, pymeasure, ipykernel to uv project `uv add pyvisa pyvisa-py numpy scikit-rf pymeasure ipykernel`
- [x] Add venv to jupyter kernels - `uv run ipython kernel install --user --name=keysight_p9375a_venv`
- [ ] Create/move essential commands to Channels class
    - [x] IFBW
    - [x] Points
    - [x] Averaging
    - [x] Averaging Enabled
    - [ ] Averaging Mode - Need docstring updated w/ options
    - [ ] Triggering Mode
    - [ ] Continuous Triggering
    - [ ] Measurement
    - [ ] Format
    - [x] Power
    - [x] Start Freq
    - [x] Stop Freq
    - [ ] Read Trace
    - [ ] Read S-Parameter (to nparray)
    - [ ] Create S-Parameter (form skrf.touchstone)
- [x] Create notebook to run though and test module
- [x] Working example for saving s1p/s2p touchstone files.
- [ ] Add traces class to Instrument
- [ ] Create function to add or remove channels and traces
