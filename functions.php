<?php 

add_action( 'admin_init', 'dailyprophet_settings_init' );

function dailyprophet_settings_init() {
 
    /* Register Settings */
    register_setting(
        'general',             	// Options group
        'quote_of_the_day'      // Option name/database
    );

    /* Create settings section */
	add_settings_section(
	    'daily-prophet-settings',  	// Section ID
	    'Additional Settings',  	// Section title
	    __return_false, 	    	// Section callback function
	    'general'                   // Settings page slug
	);

	/* Create settings field */
	add_settings_field(
	    'quote-of-the-day',       					// Field ID
	    'Quote of the Day',     					// Field title 
	    'qotd_callback', 							// Field callback function
	    'general',                    				// Settings page slug
	    'daily-prophet-settings'               		// Section ID
	);
}

function qotd_callback() { ?>

	<label for="quote-of-the-day">
        <textarea cols=50 rows=8 id="quote-of-the-day" type="text" name="quote_of_the_day" placeholder="Happiness can be found in the darkest of times, if one only remembers to turn on the light."><?php echo get_option( 'quote_of_the_day' ); ?></textarea>
    </label>

<?php }

add_action( 'rest_api_init', function () {
  register_rest_route( 'dailyprophet', '/qotd', array(
    'methods' => 'GET',
    'callback' => 'qotd_rest_callback',
  ) );
} );

function qotd_rest_callback(){
	return get_option( 'quote_of_the_day' );
}