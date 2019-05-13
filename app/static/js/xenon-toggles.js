/**
 *	Toggles
 *
 *	Non-animation
 */


;(function($, window, undefined)
{
	"use strict";

	$(document).ready(function()
	{

		$('[data-toggle="tooltip"]').each(function(i, el)
		{
			var $this = $(el),
				placement = 'bottom',
				trigger = 'hover',
				// placement = attrDefault($this, 'placement', 'top'),
				// trigger = attrDefault($this, 'trigger', 'hover'),
				tooltip_class = $this.get(0).className.match(/(tooltip-[a-z0-9]+)/i);

			$this.tooltip({
				placement: placement,
				trigger: trigger
			});

			if(tooltip_class)
			{
				$this.removeClass(tooltip_class[1]);

				$this.on('show.bs.tooltip', function(ev)
				{
					setTimeout(function()
					{
						var $tooltip = $this.next();
						$tooltip.addClass(tooltip_class[1]);

					}, 0);
				});
			}
		});

	});

})(jQuery, window);