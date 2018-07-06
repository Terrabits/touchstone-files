# Touchstone Files

Generates touchstone files for use in RF calculations and software testing.

## port-test

`port-test/` files have Re, Im values that indicate their s-parameter coordinates.

For example, for S31:

`s31 = 31.0 + j31.0`

This makes testing for the presence of the correct touchstone value trivial.
