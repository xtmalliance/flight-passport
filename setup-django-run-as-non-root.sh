#!/bin/bash

groupadd --gid 10000 django
useradd django --uid 10000 --gid 10000
mkdir static
chown django:django static
