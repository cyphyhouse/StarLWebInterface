define("ace/theme/gruvbox",["require","exports","module","ace/lib/dom"], function(require, exports, module) {

    exports.isDark = true;
    exports.cssClass = "ace-gruvbox";
    exports.cssText = ".ace-gruvbox .ace_gutter {\
background: #282828;\
color: #a89984;\
}\
.ace-gruvbox .ace_print-margin {\
width: 1px;\
background: #555651\
}\
.ace-gruvbox {\
background-color: #282828;\
color: #ebdbb2\
}\
.ace-gruvbox .ace_cursor {\
color: #F8F8F0\
}\
.ace-gruvbox .ace_marker-layer .ace_selection {\
background: #3c3836;\
}\
.ace-gruvbox.ace_multiselect .ace_selection.ace_start {\
box-shadow: 0 0 3px 0px #3c3836;\
}\
.ace-gruvbox .ace_marker-layer .ace_step {\
background: #32302f;\
}\
.ace-gruvbox .ace_marker-layer .ace_bracket {\
margin: -1px 0 0 -1px;\
border: 1px solid #f38019;\
}\
.ace-gruvbox .ace_marker-layer .ace_active-line {\
background: #3c3836;\
}\
.ace-gruvbox .ace_gutter-active-line {\
background-color: #3c3836;\
}\
.ace-gruvbox .ace_marker-layer .ace_selected-word {\
border: 1px solid #3c3836;\
}\
.ace-gruvbox .ace_invisible {\
color: #3c3836\
}\
.ace-gruvbox .ace_entity.ace_name.ace_tag,\
.ace-gruvbox .ace_keyword,\
.ace-gruvbox .ace_meta.ace_tag,\
.ace-gruvbox .ace_storage {\
color: #fb4934\
}\
.ace-gruvbox .ace_punctuation,\
.ace-gruvbox .ace_punctuation.ace_tag {\
color: #fff\
}\
.ace-gruvbox .ace_constant.ace_character,\
.ace-gruvbox .ace_constant.ace_language,\
.ace-gruvbox .ace_constant.ace_numeric,\
.ace-gruvbox .ace_constant.ace_other {\
color: #83a598\
}\
.ace-gruvbox .ace_invalid {\
color: #F8F8F0;\
background-color: #d3869b;\
}\
.ace-gruvbox .ace_invalid.ace_deprecated {\
color: #F8F8F0;\
background-color: #83a598;\
}\
.ace-gruvbox .ace_support.ace_constant,\
.ace-gruvbox .ace_support.ace_function {\
color: #83a598\
}\
.ace-gruvbox .ace_fold {\
background-color: #a3aa20;\
border-color: #F8F8F2\
}\
.ace-gruvbox .ace_storage.ace_type,\
.ace-gruvbox .ace_support.ace_class,\
.ace-gruvbox .ace_support.ace_type {\
font-style: italic;\
color: #ebaa27\
}\
.ace-gruvbox .ace_entity.ace_name.ace_function,\
.ace-gruvbox .ace_entity.ace_other,\
.ace-gruvbox .ace_entity.ace_other.ace_attribute-name,\
.ace-gruvbox .ace_variable {\
color: #a3aa20\
}\
.ace-gruvbox .ace_variable.ace_parameter {\
font-style: italic;\
color: #fabd2f\
}\
.ace-gruvbox .ace_string {\
color: #ebdbb2;\
}\
.ace-gruvbox .ace_comment {\
color: #665c54;\
font-style: italic;\
}\
.ace-gruvbox .ace_indent-guide {\
background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAEklEQVQImWPQ0FD0ZXBzd/wPAAjVAoxeSgNeAAAAAElFTkSuQmCC) right repeat-y\
}";

    var dom = require("../lib/dom");
    dom.importCssString(exports.cssText, exports.cssClass);
});
