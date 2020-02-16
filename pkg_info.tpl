<h2>{{ pkg_name }}</h2>
%for paragraph in pkg["description"]:
  <p>{{ paragraph }}</p>
%end
<h3>Dependencies:</h3>
<ul>
  %if not pkg["dependencies"]:
    <li>None were found</li>
  %else:
    %for dep in pkg["dependencies"]:
      <li>
        <a href={{ dep }}>
          {{ dep }}
        </a>
      </li>
    %end
  %end
</ul>
<h3>Reverse dependencies:</h3>
<ul>
  %if not pkg["reverse_dependencies"]:
    <li>None were found</li>
  %else:
    %for dep in pkg["reverse_dependencies"]:
      <li>
        <a href={{ dep }}>
          {{ dep }}
        </a>
      </li>
    %end
  %end
</ul>
<a href="/">Index</a>