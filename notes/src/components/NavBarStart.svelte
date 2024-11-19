<script>
  import NavBarHeading from "./NavBarHeading.svelte";

  // Make a prop called 'title' for our site title.
  export let title;
</script>

<div class="navbar-start">
  <div class="flex flex-row">
    <!-- The main site icon.  We use google material icons for this. -->
    <i class="material-icons text-primary-content px-5">school</i>

    <!-- The main site title. -->
    <NavBarHeading {title} isPadded={false} />
  </div>
</div>
