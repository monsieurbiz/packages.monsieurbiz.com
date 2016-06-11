#!/bin/bash
git fetch
git checkout packages
git reset --hard origin/packages
php bin/satis build satis.json web/
