function setup() {
    load 'test_helper/bats-support/load'
    load 'test_helper/bats-assert/load'

    # get the containing directory of this file
    # use $BATS_TEST_FILENAME instad of ${BASH_SOURCE[0]} or $0,
    # as those will point to the bats executable's location or the preprocessed file respectively
    DIR="$( cd "$( dirname "$BATS_TEST_FILENAME" )" >/dev/null 2>&1 && pwd )"
    PATH="$DIR/..:$PATH"
}

# function setup_file() {
#     # Start a daemon for REST testing
#     ./fuzzy.py --rest :5001 &
#     fuzzypid=$!
# }


# function teardown_file() {
#     kill ${fuzzypid}
# }



@test "Make sure it runs" {
    run convert.py
    assert_output --partial 'Latitude =  42.291409849999994'
    assert_output --partial 'Longitude =  -71.39804914300714'
}

