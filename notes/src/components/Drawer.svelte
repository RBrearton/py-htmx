<script>
  export let isRightDrawer;

  let drawerTypeString = isRightDrawer ? "drawer-end" : "";
  let drawerId = isRightDrawer ? "right-drawer-toggle" : "left-drawer-toggle";
</script>

<div class="drawer xl:drawer-open {drawerTypeString}">
  <!-- This checkbox internally determines whether the drawer is open. -->
  <input type="checkbox" class="drawer-toggle" id={drawerId} />

  <!-- The main contents of the page. -->
  <div class="drawer-content p-16 flex flex-col">
    <slot name="pageContent">if you see this, i messed up</slot>
  </div>

  <!-- What goes in the drawer itself. -->
  <div class="drawer-side flex-shrink-0 p-5">
    <slot name="drawerContent">if you see this, i messed up</slot>
  </div>
</div>
