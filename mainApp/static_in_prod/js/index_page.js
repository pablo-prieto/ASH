<script type="text/javascript" language="javascript">
    jQuery.fn.center = function () {
        this.css("position","absolute");
        this.css("top", ( $(window).height() - this.height() ) / 2+$(window).scrollTop() + "px");
        this.css("left", ( $(window).width() - this.width() ) / 2+$(window).scrollLeft() + "px");
        return this;
    }

    $(document).ready(function() {      
        $("#thumbnail img").click(function(e){
        
            $("#background").css({"opacity" : "0.7"})
                            .fadeIn("fast");            
                        
            $("#large").html("<br><br><br><br><br>This is just a demo of a pup-up option.")
                       .center()
                       .fadeIn("fast");         
            
            return false;
        });
            
        $(document).keypress(function(e){
            if(e.keyCode==27){
                $("#background").fadeOut("fast");
                $("#large").fadeOut("fast");
            }
        });
        
        $("#background").click(function(){
            $("#background").fadeOut("fast");
            $("#large").fadeOut("fast");
        });
        
        $("#large").click(function(){
            $("#background").fadeOut("fast");
            $("#large").fadeOut("fast");
        });
        
    });
</script>