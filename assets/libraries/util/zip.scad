/**
* zip.scad
*
* @copyright Justin Lin, 2020
* @license https://opensource.org/licenses/lgpl-3.0.html
*
* @see https://openhome.cc/eGossip/OpenSCAD/lib2x-zip.html
*
**/ 

use <_impl/_zip_impl.scad>;

function zip(lts) = _zipAll(lts);