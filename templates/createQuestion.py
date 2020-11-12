{% extends 'MasterPage.html' %}
{% block content %}



<form>
{% for i in range(questionCount) %}
    <div class="form-group">
        <label for="exampleInputEmail1">Email address</label>
        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
        <small id="emailHelp" class="form-text text-muted">Well never share your email with anyone else.</small>
  </div>
{% endfor %}

</form>
{% endblock %}
