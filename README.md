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
    - [ ] IFBW
    - [ ] Points
    - [ ] Averaging
    - [ ] Averaging Enabled
    - [ ] Triggering
    - [ ] Measurement
    - [ ] Format
    - [ ] Power
    - [ ] Start Freq
    - [ ] Stop Freq
    - [ ] Read S-Parameter (to nparray)
    - [ ] Create S-Parameter (form skrf.touchstone)
- [ ] Create notebook to run though and test module
- [ ] 