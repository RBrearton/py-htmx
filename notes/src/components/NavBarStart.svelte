<script>
  // Make a prop called 'title' for our site title.
  export let title;
</script>

<div class="navbar-start">
  <div class="flex flex-row">
    <!-- The main site icon.  We use google material icons for this. -->
    <i class="material-icons text-primary-content">notes</i>

    <!-- The main site title. -->
    <h4 class="text-primary-content">
      {title}
    </h4>
  </div>
</div>
