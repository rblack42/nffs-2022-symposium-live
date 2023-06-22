//####################################
// square_spar.scad
// (c) 2021 by Roie R. Black
//====================================


module square_spar(length=6,size=1/16) {
  translate([size/2, 0, size/2])
    cube([size,length,size], center=true);
}

square_spar(6,1/16);
