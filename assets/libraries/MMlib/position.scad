//#####################################
// position.scad
// (c) 2021 by Roie R. Black
//=====================================

// apply rotation, then translation
module align(d) {
  translate([d[0],d[1],d[2]])
    rotate([d[3],d[4],d[5]]) children();
}

// apply translation only
module position(d) {
  translate([d[0],d[1],d[2]]) children();
}