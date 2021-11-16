#!
setup () {
    load $POET_VENDOR/github.com/bats-core/bats-support/load.bash
    load $POET_VENDOR/github.com/bats-core/bats-assert/load.bash
    #load 'test_helper/bats-assert/load'
}
@test "can run our script" {
    poem
}
@test "add2" {
    poet ex add2 3 4
}
@test "exit-with-error 0" {
    run poet ex exit-with-error 0
    assert_output "input was [0]"
    [ $status = 0 ]
}
@test "exit-with-error 1" {
    run poet ex exit-with-error 1
    assert_output "input was [1]"
    [ $status = 1 ]
}
