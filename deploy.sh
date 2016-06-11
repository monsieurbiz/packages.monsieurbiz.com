#!/bin/bash
git fetch
git checkout packages
git reset --hard origin/packages
composer install -o --no-dev
php bin/satis build satis.json web/
