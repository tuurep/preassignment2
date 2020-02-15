<b>List of packages:</b>
<ul>
%for name in pkg_names:
  <li>
    <a href={{ name }}>
      {{ name }}
    </a>
  </li>
%end
</ul>