$(function(){
    $('.gradeList').on('change', function() {
        $("form").attr('novalidate', 'novalidate');
        if (this.value == 'admin')
        {
            $(".universal").show();
            $(".serverName").show();
            $(".adminLabel").show();
            $(".admin").show();
            $(".helperLabel").hide();
            $(".helper").hide().prop('required',false);
            $(".builderLabel").hide();
            $(".builder").hide().prop('required',false);
            $(".recoverLabel").hide();
            $(".recover").hide().prop('required',false);
            $(".recover_Q1[type='file']").hide().prop('required',false);
        }
        else if (this.value == 'helper')
        {
            $(".universal").show();
            $(".serverName").show();
            $(".adminLabel").hide();
            $(".admin").hide().prop('required',false);
            $(".helperLabel").show();
            $(".helper").show();
            $(".helper_Q2[type='file']").show();
            $(".builderLabel").hide();
            $(".builder").hide().prop('required',false);
            $(".recoverLabel").hide();
            $(".recover").hide().prop('required',false);
            $(".recover_Q1[type='file']").hide().prop('required',false);
        }
        else if (this.value == "builder")
        {
            $(".universal").show();
            $(".serverName").show();
            $(".adminLabel").hide();
            $(".admin").hide().prop('required',false);
            $(".helperLabel").hide();
            $(".helper").hide().prop('required',false);
            $(".helper_Q2[type='file']").hide().prop('required',false);
            $(".builderLabel").show();
            $(".builder").show();
            $(".builder_Q2[type='file']").show();
            $(".recoverLabel").hide();
            $(".recover").hide().prop('required',false);
            $(".recover_Q1[type='file']").hide().prop('required',false);
        }
        else if (this.value == 'recover')
        {
            $(".universal").hide().prop('required',false);
            $(".serverName").hide().prop('required',false);
            $(".adminLabel").hide();
            $(".admin").hide().prop('required',false);
            $(".helperLabel").hide();
            $(".helper").hide().prop('required',false);
            $(".helper_Q2[type='file']").hide().prop('required',false);
            $(".builderLabel").hide();
            $(".builder").hide().prop('required',false);
            $(".builder_Q2[type='file']").hide().prop('required',false);
            $(".recoverLabel").show();
            $(".recover").show();
            $(".recover_Q1[type='file']").show();
        }
      })
  });