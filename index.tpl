<h2>List of packages:</h2>
<ul>
  %for pkg in pkgs_ordered:
    <li>
      <a href={{ pkg }}>
        {{ pkg }}
      </a>
    </li>
  %end
</ul>