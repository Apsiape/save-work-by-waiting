# Only quantum channels save work by waiting

Seth Douglas and Nidhal Mghirbi — October 2026.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23310624.svg)](https://doi.org/10.5281/zenodo.23310624)

[Read the manuscript](paper/main.pdf) · [TeX source](paper/main.tex) ·
[Machine checks](verification/README.md)

Faist, Berta and Brandão showed that n uses of a time-covariant quantum channel cost, to leading order, n times its
thermodynamic capacity, when the device may collect all inputs before it releases any output. Many devices cannot wait:
they must release each output before the next input arrives. This paper shows that, for devices built from
energy-conserving dynamics and heat baths, this can cost extra work, but only for quantum channels, and determines exactly how much.

- **Real-time work law.** For a time-covariant channel the real-time work per use is a maximum over inputs of an
  entropy change plus an energy change, with one extra term: the least correlation an implementation must leave
  between each output and what stays in the device. Below this rate, with thermal hardware and deterministic work, the worst-case error of
  every real-time device tends to one.
- **Only quantum channels pay.** Classical channels, including full reset, pay no surcharge. Partial reset of a qubit
  pays one at every temperature, and the Werner–Holevo qutrit channel pays kT ln 3 per use, against essentially
  nothing in batch.
- **What is free, and undecidability.** In real time a channel costs nothing exactly when it is a limit of thermal
  operations, and no algorithm decides which channels these are, even in a fixed dimension.
- **Clocks.** If the battery holds no phase reference of its own, a clock that must come back exactly cannot run a
  channel that is not time-covariant; one that may come
  back slightly changed, with its actual mean energy and entropy refunded, runs every channel at the same rate, and for a gate the heat baths must reach energies that
  grow faster than the number of uses.

All rates here are optimal asymptotic work rates at vanishing error over the complete interaction, with hardware
allowed to grow; where a controller comes back only approximately, its actual mean energy and entropy are also
refunded up to sublinear changes.

This repository contains the manuscript, its source, and the machine checks that accompany it. It is version 1.0.1 ([doi:10.5281/zenodo.23310736](https://doi.org/10.5281/zenodo.23310736)) of the Zenodo record [doi:10.5281/zenodo.23310624](https://doi.org/10.5281/zenodo.23310624); that concept DOI always resolves to the latest version. Version 1.0.0 is [doi:10.5281/zenodo.23310625](https://doi.org/10.5281/zenodo.23310625). The manuscript is the
authority for exact statements and hypotheses; [verification/README.md](verification/README.md) lists what is checked
by machine and what is proved only in the text.

## Reproduce

Requires Python 3.10+ with the packages in [verification/requirements.txt](verification/requirements.txt), a TeX
distribution with the packages listed in paper/main.tex, and, for the formal proofs, Lean 4 with Mathlib as described
in [verification/README.md](verification/README.md).

    python -m pip install -r verification/requirements.txt
    python paper/build.py
    python verification/run_all.py

The build refuses to finish on any undefined reference or citation, duplicate label or overfull line. Each check
prints what it verifies and exits with status 0 when it passes.
Until Mathlib is set up as described there, the Lean step reports that it was skipped and the run
fails; the Python checks do not need it.

## Companions

This paper is one of four on the thermodynamics of time order, each with its own repository:
- [The work cost of answering in real time](https://github.com/Apsiape/answering-in-real-time) · [doi:10.5281/zenodo.23310628](https://doi.org/10.5281/zenodo.23310628)
- [The price of keeping time](https://github.com/Apsiape/price-of-keeping-time) · [doi:10.5281/zenodo.23310632](https://doi.org/10.5281/zenodo.23310632)
- [The price of time order](https://github.com/Apsiape/price-of-time-order) · [doi:10.5281/zenodo.23310622](https://doi.org/10.5281/zenodo.23310622)

Earlier papers it builds on are listed, with the exact results used and where, in the appendix "Results from the
companion papers" of the manuscript.

## Reading guide

For the organizing principle, read the introduction, Figure 1 and Table 2 of *The price of time order*. For the device model,
the law for repeated channels and the free set, read *Only quantum channels save work by waiting*. For processes with
memory and the classical example of an order cost, read *The work cost of answering in real time*. For returned
clocks, the batch law and the time reverse, read *The price of keeping time*. Readers following proofs should note that
the finite-source module of *The work cost of answering in real time* (Appendix E, Lemma 12) is established
independently of the channel results it helps to prove.

## License and citation

The manuscript and repository content are available under **CC BY 4.0**. The software and machine-readable
verification artifacts are additionally available under the **MIT License**, at your option; see
[RIGHTS.md](RIGHTS.md) for the scope. [CITATION.cff](CITATION.cff) provides machine-readable citation metadata. Please cite the manuscript by its concept DOI, [10.5281/zenodo.23310624](https://doi.org/10.5281/zenodo.23310624).
