//######################################
// trimming_square_spar
// (c) 2021 - Roie R. Black
//**************************************

module trimming_square_spar(length=5, size=1/16, angle=30) {
  calcl = length+1;
  dx = 0.5;

  rotate([0,0,90+angle])
  translate([-dx,-size/2,-size/2])
    cube([calcl,size,size]);
}

trimming_square_spar();
