#!/bin/bash

echo '<?xml version="1.0" encoding="UTF-8"?>' > addons.xml

echo "<addons>" >> addons.xml
for plugin in `ls -d */`
do
    tail --lines=+2  $plugin/addon.xml >> addons.xml
done
echo "</addons>" >> addons.xml
md5sum addons.xml > addons.xml.md5