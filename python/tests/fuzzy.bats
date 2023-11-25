setup() {
    load 'test_helper/bats-support/load'
    load 'test_helper/bats-assert/load'

    # get the containing directory of this file
    # use $BATS_TEST_FILENAME instad of ${BASH_SOURCE[0]} or $0,
    # as those will point to the bats executable's location or the preprocessed file respectively
    DIR="$( cd "$( dirname "$BATS_TEST_FILENAME" )" >/dev/null 2>&1 && pwd )"
    PATH="$DIR/..:$PATH"
}


@test "Check 100% match -- ./fuzzy.py 'This is a test string'" {
    run fuzzy.py 'This is a test string'
    assert_output --partial '100% This is a test string' 
}

@test "Check 97% match -- ./fuzzy.py 'this is a test string'" {
    run fuzzy.py 'this is a test string'
    assert_output --partial '97% This is a test string' 
}

@test "Check 81% match -- ./fuzzy.py 'this is some'" {
    run fuzzy.py 'this is some'
    assert_output --partial '81% This is something' 
}


@test "Check 50% match -- ./fuzzy.py 'smurf'" {
    run fuzzy.py 'smurf'
    assert_output --partial '50% This is something else'
}