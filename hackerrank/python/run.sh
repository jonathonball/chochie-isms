#!/bin/zsh

function create_files {
    echo -e "Do you want to create files for a challenge named \"${challenge_name}\" [yes or no]: \c";
    read ans;
    if [[ $ans =~ [Yy] ]]; then
        echo "Creating..."
        if ! [ -f $script_file ]; then
            touch $script_file;
            echo "${script_file}";
        fi;

        if ! [ -f $input_file ]; then
            touch $input_file;
            echo "${input_file}";
        fi;

        if ! [ -f $output_file ]; then
            touch $output_file;
            echo "${output_file}";
        fi;
    else
        exit 0;
    fi;
};

function check_args {
    if [ -z $1 ]; then
        echo "Missing script name as first argument" 1>&2;
        exit 1;
    fi;

    if ! [ -f $script_file ]; then
        echo "Cannot find script: ${script_file}" 1>&2;
        create_files;
    fi;

    if ! [ -f $input_file ]; then
        echo "Cannot find input: ${input_file}" 1>&2;
        create_files;
    fi;

    if ! [ -f $output_file ]; then
        echo "Cannot find output: ${output_file}" 1>&2;
        create_files;
    fi;
};

function run_the_thing {
    /usr/bin/env python3 $script_file < $input_file;
};

challenge_name="$(basename ${1} .py)";
script_file="${challenge_name}.py";
input_file="input/${challenge_name}.txt";
output_file="output/${challenge_name}.txt";
script_output="";

check_args $1;
run_the_thing;
