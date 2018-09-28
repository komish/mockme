#!/usr/bin/env bash

set -ex

# We expect this to stay mostly static
# but should it change, we don't want it existing
# in multiple places
URL="https://goo.gl/g54u4V"

TEST_ONE=$(mockme "This is a test script")
EXPECTED_ONE="ThIs iS A TeSt sCrIpT "

TEST_TWO=$(mockme This is a test script)
EXPECTED_TWO="ThIs Is A TeSt ScRiPt "

# First Example Tests
test ! -z "${TEST_ONE}"
test "${TEST_ONE}" = "${URL}: ${EXPECTED_ONE}"

# Second Example Tests
test ! -z "${TEST_TWO}"
test "${TEST_TWO}" = "${URL}: ${EXPECTED_TWO}"

# Marker
echo "Testing Completed";
exit 0
