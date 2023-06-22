// functions.scad

// given angle and length, return offset
function delta(ang, l)  = l / cos(ang);

// given chord nd camber, return radius
function radius(ch, ca) = ch * ch /(8 * ca * ch/100) + ca*ch/100/2;

// given two offsets s apart, return offset at 0<= x <=s
function cx0(x,c1,c2,s) = c1 + (c2-c1)/s * x;

// apply rotation, then translation
module align(d)
  translate([d[0],d[1],d[2]])
    rotate([d[3],d[4],d[5]]) children();

module position(d)
  translate([d[0],d[1],d[2]]) children();
