function setup() {
    load 'test_helper/bats-support/load'
    load 'test_helper/bats-assert/load'

    # get the containing directory of this file
    # use $BATS_TEST_FILENAME instad of ${BASH_SOURCE[0]} or $0,
    # as those will point to the bats executable's location or the preprocessed file respectively
    DIR="$( cd "$( dirname "$BATS_TEST_FILENAME" )" >/dev/null 2>&1 && pwd )"
    PATH="$DIR/..:$PATH"
}

function setup_file() {
    # Start a daemon for REST testing
    ./fuzzy.py --rest &
    fuzzypid=$!
}


function teardown_file() {
    kill ${fuzzypid}
}




@test "Check 100% match -- ./fuzzy.py 'This is a test string'" {
    run fuzzy.py --check 'This is a test string'
    assert_output --partial '100% This is a test string' 
}

@test "Check  97% match -- ./fuzzy.py 'this is a test string'" {
    run fuzzy.py --check 'this is a test string'
    assert_output --partial '97% This is a test string' 
}

@test "Check  81% match -- ./fuzzy.py 'this is some'" {
    run fuzzy.py --check 'this is some'
    assert_output --partial '81% This is something' 
}


@test "Check  50% match -- ./fuzzy.py 'smurf'" {
    run fuzzy.py --check 'smurf'
    assert_output --partial '50% This is something else'
}


@test "Check REST API 100% match -- curl -X PUT 'http://localhost:5000/check/'$( echo 'This is a test string'|sed 's/ /%20/g')" {
    urlpart=$(echo 'This is a test string'| sed 's/ /%20/g')
    run curl --silent -X PUT "http://localhost:5000/check/$urlpart"
    assert_output --partial 'fuzzy match is 100% This is a test string'
}

@test "Check REST API  97% match -- curl -X PUT 'http://localhost:5000/check/'$( echo 'this is a test string'|sed 's/ /%20/g')" {
    urlpart=$(echo 'this is a test string'| sed 's/ /%20/g')
    run curl --silent -X PUT "http://localhost:5000/check/$urlpart"
    assert_output --partial 'fuzzy match is 97% This is a test string'
}
