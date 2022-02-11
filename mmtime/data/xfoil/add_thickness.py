def add_thickness(x,y, T):
    """ x,y are camber points, T is thickness
    maxAngle = 12
    # make sure X and Y are the same length
    if len(x) != len(y):
        print("ERROR x and y vectors are not the same size!!!")
        return

    nx = len(x)

    # generate slopes of camber line
    dy = [0 for i in range(nx)]
    dydx = dy
    for d in range(nx):
        if d==nx:
            dy[d]=(y[d]-y[d-1])
            dx[d]=(x[d]-x[d-1])
        elif d==1:
            dy[d]=(y[d+1]-y[d])
            dx[d]=(x[d+1]-x[d])
        else
            dy[d]=(y[d+1]-y[d-1])
            dx[d]=(x[d+1]-x[d-1])
        dydx[d] = dy[d]/dx[d]

    nptot = math.round(180/maxLEangle);
    np1 = math.round((((math.pi/2) - math.atan(dydx(1))) / (math.pi)) * nptot)
    np2 = math.round((((math.pi/2) + math.atan(dydx(1))) / (math.pi)) * nptot)

    # this section generates the thickness distribution for the airfoil
    # assuming a rounded leading edge and a parabolic trailing edge
    % T is the thickness of the current airfoil
    xTte = [1:5]; % Defines number of points that are effected at the TE
        # (Note the equation that appears in next line must be changes if 5 is not used)
    Tte = [-T/50*xTte.^2+T/2]; % define thickness distribution over last 5 y points
    Tdv = [T/2*ones(1,sizey-5) Tte]; % sets the thickness distribution vector,

    #  constant thickness until the last 5 y values
    # this section adjusts the coordinates for thickness distribution for p = 1:1:sizey
    ty(p) = Tdv(p)*cos(atan(dydx(p))); % adjust y coordinate for slope of MCL
    tx(p) = Tdv(p)*sin(atan(dydx(p))); % adjuste x coordinate for slope of MCL end
    ysurtop = y + ty; ysurbot = y - ty; xsurtop = x - tx;
    xsurbot = x + tx;

    % Creating the leading edge
    theta0le = atan(dydx(1));
    thetaletop = (theta0le+pi/2):(pi/2-theta0le)/np1:pi; % counter-cloclwise around the leading edge to form top
    thetalebot = pi:(theta0le+pi/2)/np2:(theta0le+3*pi/2); % counter-clockwise around the leading edge to form bottom

    % top surface of LE (+y)
    at=0;
    for kt = 2:1:np1+1 % adjusted so that point where circle and upper surface
        # meet is not defined 2 times but LE point is defined by both the upper and lower surfaces
        at = at+1;
        xletop(at) = T/2+T/2*cos(thetaletop(kt)); % adjusted for LE raidus so that min(x)=0 not a (-) number
        yletop(at) = T/2*sin(thetaletop(kt));

    % botom surface of LE (-y)
    ab=0;
    for kb = 1:1:np2 % adjusted so that point where circle and upper surface meet is not defined
        # 2 times but LE point is defined by both the upper and lower surfaces
        ab = ab+1;
        xlebot(ab) = T/2+T/2*cos(thetalebot(kb)); % adjusted for LE raidus so that min(x)=0 not a (-) number
        ylebot(ab) = T/2*sin(thetalebot(kb)); end
        b=0;
        for v = sizey:-1:1; % re-organize xb and zb so that x goes down up not up
            b=b+1;
            xsurtopr(b)=xsurtop(v);
            ysurtopr(b)=ysurtop(v);
            xout = [xlebot xsurbot]';
            yout = [ylebot ysurbot]';
            out = [xout yout];
            xback = [xsurtopr xletop]';
            yback = [ysurtopr yletop]';
            back = [xback yback];
            airfoilpoints = [back ; out];
