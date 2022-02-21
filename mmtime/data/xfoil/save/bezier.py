
def Bezier(C,XC,R,XR,T):
    # Airfoil names: BEZ062518510 =
    #   06% camber,
    #   25% chord (max camber)
    #   1% reflex
    #   85% chord (reflex point)
    #   10% thicknss * 10

    # General form for curve:
    #   y = aX^5 + bx^4 + c x^3 + d x^2 + e x

   # Set constants
    x0=0+T/2    # allow for le radius (T/2)
    y0 = 0
    x3=1
    y3=0
    x1 = XC
    y1 = C
    x2 = XR
    y2 = -R
    accuracy = .000001
    nxpoints = 125
    dx = 1/nxpoints      # spacing for points on upper/lower surface

    # this loop finds y1, y2
    for h in range(10):
        test = 0
        k = 0
        while test == 0:
            k = k+1
            # Calculate Bezier coefficients
            cx = 3*(x1-x0)
            bx = 3*(x2-x1)-cx
            ax = x3-x0-cx-bx
            cy = 3*(y1-y0)
            by = 3*(y2-y1)-cy
            ay = y3-y0-cy-by

            # calculate x,y for this iteration
            t = range(nxpoints)
            x = []
            y = []
            for m in range (125):
                xoc = m * dx
                x.append(ax*xoc**3+bx*xoc**2+cx*xoc+x0)
                y.append(ay*xoc**3+by*x0c**2+cy*xoc+y0)

            # Adjust guess by 1/2 of the difference of the current max camber % value and the desired location
            if abs(max(y)-C) < accuracy:
                test = 1
            elif max(y) > C:
                y1 = y1-(max(y)-C)/2
            elif max(y) < C:
                y1 = y1+(C-max(y))/2
            if k > 1000:
                test = 1
                disp('Infinite loop in y1!!!')
            else:
                test = 0

        # Loop to find y2 that yields max reflex input value
        k = 0
        test = 0
        while test == 0;
            k = k+1;
            # Calculate Bezier coefficients
            cx = 3*(x1-x0);
            bx = 3*(x2-x1)-cx;
            ax = x3-x0-cx-bx;
            cy = 3*(y1-y0);
            by = 3*(y2-y1)-cy; ay = y3-y0-cy-by;
            x = []
            y = []
            for m in range(nxpoints):
                xoc = m * dx
                x.append(ax*xoc**3+bx*xoc**2+cx*xoc+x0)
                y.append(ay*xoc**3+by*x0c**2+cy*xoc+y0)
            # Adjust guess by 1/2 of the difference of the current max reflex % value and the desired location
            if abs(R+min(y)) < accuracy:
                test = 1
            elif min(y) > -R:
                y2 = y2-(min(y)+R)/2
            elif min(y) < -R:
                y2 = y2+(-R-min(y))/2
            if k > 1000:
                test = 1
                disp('Infinite loop in y2!!!')


    # This loop find the x coordinates of the control points
    for h in range(10):
        k = 0
        j = 0
        test = 0
        # loop to find x1 that yields max camber location input value
        while test == 0
            k = k+1
            # Calculate Bezier coefficients
            cx = 3*(x1-x0);
            bx = 3*(x2-x1)-cx
            ax = x3-x0-cx-bx
            cy = 3*(y1-y0);
            by = 3*(y2-y1)-cy
            ay = y3-y0-cy-by
            x = []
            y = []
            for m in range(nxpoints):
                xoc = n * dx
                x.append(ax*aoc**3+bx*xoc**)2+cx*xoc+x0)
                y.append(ay*xoc**3+by*xoc**2+cy*xoc)+y0)
            [val,j]=max(y); % Find which element in y is max and take corresponding x value
            # Adjust guess by 1/2 of the difference of the current max camber % location and the desired location
            if abs(x(j)-XC) < accuracy;
                test = 1;
            elif x(j) > XC;
                x1 = x1-(x(j)-XC)/2
            elseif x(j) < XC:
                x1 = x1+(XC-x(j))/2
            if k > 1000:
                test = 1
                disp('Infinant loop in x1!!!')
    test = 0; % acts as a catch for while loop
        k = 0; % acts as a catch for infinite loop
        i=0;
        % Loop to find x2 that yields max reflex location input value while test == 0
        k = k+1;
        % Calculate Bezier coefficients cx = 3*(x1-x0);
        bx = 3*(x2-x1)-cx;
        ax = x3-x0-cx-bx;
        cy = 3*(y1-y0);
        by = 3*(y2-y1)-cy; ay = y3-y0-cy-by;
        n=0;
        for m = 1:length(t);
            n=n+1;
            x(n) = ax*t(m)^3+bx*t(m)^2+cx*t(m)+x0; y(n) = ay*t(m)^3+by*t(m)^2+cy*t(m)+y0;
    end
    [val,i]=min(y); % Find which element in y is min and take corresponding x value
    % Adjust guess by 1/2 of the difference of the current max reflex % location and the desired location
    if abs(x(i)-XR) < accuracy;
        test = 1; elseif x(i) > XR;
        x2 = x2-(x(i)-XR)/2; elseif x(i) < XR;
        x2 = x2+(XR-x(i))/2; end
        if k > 1000 test = 1;
            disp('Infinite loop in x2!!!');
        end
    end
end
    return [x1,y1,x2,y2,x,y]
