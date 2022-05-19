$().ready(function () {
  console.log("Page loaded!");
  btnEvent();
});

let btnEvent = () => {
  $("#form").on("submit", function (e) {
    // get text data
    req = $.ajax({
      url: "/",
      type: "POST",
      //   content: "application/json",
      data: { txt: $("#postBodyText").val() },
    }).done(function (data) {
      $("#output").text(data.output).show();
    });
    e.preventDefault();
  });
};
