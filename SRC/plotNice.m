function plotNice( theTitle, theXLabel, theYLabel, varargin )
%plotNice Plot data with decent default values.  Similar to 'plot'.
%         Use : plotNice( theTitle, theXLabel, theYLabel, X,Y,... )

m = {'-o','-.','*','.','x','s','d','^','v','>','<','p','h'};
set_marker_order = @() set(gca(), ...
    'LineStyleOrder',m, 'ColorOrder',[0 0 0], ...
    'NextPlot','replacechildren');
set_marker_order();

h=plot(varargin{:});
h.Marker = 'o';
h.LineWidth = 2;
h.MarkerSize = 20;  

title(theTitle);
xlabel(theXLabel);
ylabel(theYLabel);

set(gca,'FontSize',20);
set(gcf,'color',[1 1 1]);

end

