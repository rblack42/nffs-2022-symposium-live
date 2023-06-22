// square_spar

module square_spar(length=6,size=1/16) {
	cube([size,length,size], center=true);
}

square_spar(6,1/16);
