# make_stub_files: Fri 12 Feb 2016 at 10:07:42

from typing import Any, Dict, Optional, Sequence, Tuple, Union
# At present, I don't understand how to tell mypy about ast.Node
# import ast
# Node = ast.Node
Node = Any
def dump(title: Any, s: str=None) -> None: ...
def dump_dict(title: Any, d: Any) -> None: ...
def dump_list(title: Any, aList: List[Any]) -> None: ...
def is_known_type(s: str) -> Union[Any, bool]: ...
    #   0: return True
    #   0: return bool
    #   1: return True
    #   1: return bool
    #   2: return is_known_type(inner) if inner else True
    #   2: return Any
    #   3: return is_known_type(inner) if inner else True
    #   3: return Any
    #   4: return True
    #   4: return bool
    #   5: return True
    #   5: return bool
    #   6: return all(is_known_type(z.strip()) for z in split_types(s3))
    #   6: return bool
    #   7: return True
    #   7: return bool
    #   8: return False
    #   8: return bool
def main() -> None: ...
def merge_types(a1: Any, a2: Any) -> str: ...
    #   0: return sorted(set(r1+r2))
    #   0: return str
def pdb(self) -> None: ...
def reduce_numbers(aList: List[Any]) -> List[Any]: ...
    #   0: return aList
    #   0: return List[Any]
def reduce_types(aList: List[Any], name: str=None, trace: bool=False) -> Any: ...
    #   0: return s
    #   0: return str
    #   1: return show('None')
    # ? 1: return show(str)
    #   2: return show('Any',known=False)
    # ? 2: return show(str, known=bool)
    #   3: return show(r[0])
    # ? 3: return show(str)
    #   4: return show('Optional[%s]'%r[0])
    # ? 4: return show(str)
    #   5: return show(r[0])
    # ? 5: return show(str)
    #   6: return show('Union[%s]'%', '.join(sorted(r)))
    # ? 6: return show(str)
    def show(s: str, known: Any=True) -> str: ...
        #   0: return s
        #   0: return str
def split_types(s: str) -> List[Any]: ...
    #   0: return aList
    #   0: return List[Any]
def truncate(s: str, n: int) -> str: ...
    #   0: return s if len(s)<=n else s[:n-3]+'...'
    #   0: return str
class AstFormatter:
    def format(self, node: Node) -> Union[Any, str]: ...
        #   0: return val and val.strip() or ''
        #   0: return Union[Any, str]
    def visit(self, node: Node) -> str: ...
        #   0: return ','.join(self.visit(z) for z in node)
        #   0: return str
        #   1: return 'None'
        #   1: return str
        #   2: return s
        #   2: return str
    def do_ClassDef(self, node: Node) -> str: ...
    def do_FunctionDef(self, node: Node) -> str: ...
    def do_Interactive(self, node: Node) -> None: ...
    def do_Module(self, node: Node) -> str: ...
    def do_Lambda(self, node: Node) -> str: ...
    def do_Expr(self, node: Node) -> str: ...
    def do_Expression(self, node: Node) -> str: ...
    def do_GeneratorExp(self, node: Node) -> str: ...
    def do_AugLoad(self, node: Node) -> str: ...
    def do_Del(self, node: Node) -> str: ...
    def do_Load(self, node: Node) -> str: ...
    def do_Param(self, node: Node) -> str: ...
    def do_Store(self, node: Node) -> str: ...
    def do_arguments(self, node: Node) -> str: ...
    def do_arg(self, node: Node) -> str: ...
    def do_Attribute(self, node: Node) -> str: ...
    def do_Bytes(self, node: Node) -> str: ...
    def do_Call(self, node: Node) -> str: ...
    def do_keyword(self, node: Node) -> str: ...
    def do_comprehension(self, node: Node) -> str: ...
    def do_Dict(self, node: Node) -> str: ...
    def do_Ellipsis(self, node: Node) -> str: ...
    def do_ExtSlice(self, node: Node) -> str: ...
    def do_Index(self, node: Node) -> str: ...
    def do_List(self, node: Node) -> str: ...
    def do_ListComp(self, node: Node) -> str: ...
    def do_Name(self, node: Node) -> str: ...
    def do_Num(self, node: Node) -> str: ...
    def do_Repr(self, node: Node) -> str: ...
    def do_Slice(self, node: Node) -> str: ...
    def do_Str(self, node: Node) -> str: ...
    def do_Subscript(self, node: Node) -> str: ...
    def do_Tuple(self, node: Node) -> str: ...
    def do_BinOp(self, node: Node) -> str: ...
    def do_BoolOp(self, node: Node) -> str: ...
    def do_Compare(self, node: Node) -> str: ...
    def do_UnaryOp(self, node: Node) -> str: ...
    def do_IfExp(self, node: Node) -> str: ...
    def do_Assert(self, node: Node) -> str: ...
    def do_Assign(self, node: Node) -> str: ...
    def do_AugAssign(self, node: Node) -> str: ...
    def do_Break(self, node: Node) -> str: ...
    def do_Continue(self, node: Node) -> str: ...
    def do_Delete(self, node: Node) -> str: ...
    def do_ExceptHandler(self, node: Node) -> str: ...
    def do_Exec(self, node: Node) -> str: ...
    def do_For(self, node: Node) -> str: ...
    def do_Global(self, node: Node) -> str: ...
    def do_If(self, node: Node) -> str: ...
    def do_Import(self, node: Node) -> str: ...
    def get_import_names(self, node: Node) -> Any: ...
        #   0: return result
        # ? 0: return result
    def do_ImportFrom(self, node: Node) -> str: ...
    def do_Pass(self, node: Node) -> str: ...
    def do_Print(self, node: Node) -> str: ...
    def do_Raise(self, node: Node) -> str: ...
    def do_Return(self, node: Node) -> str: ...
    def do_TryExcept(self, node: Node) -> str: ...
    def do_TryFinally(self, node: Node) -> str: ...
    def do_While(self, node: Node) -> str: ...
    def do_With(self, node: Node) -> str: ...
    def do_Yield(self, node: Node) -> str: ...
    def kind(self, node: Node) -> Any: ...
        #   0: return node.__class__.__name__
        # ? 0: return Node.__class__.__name__
    def indent(self, s: str) -> str: ...
        #   0: return '%s%s'%(' '*4*self.level, s)
        #   0: return str
    def op_name(self, node: Node, strict: bool=True) -> str: ...
        #   0: return name
        #   0: return str
class AstArgFormatter(AstFormatter):
    def do_BoolOp(self, node: Node) -> str: ...
        #   0: return 'bool'
        #   0: return str
    def do_Bytes(self, node: Node) -> str: ...
        #   0: return 'bytes'
        #   0: return str
    def do_Name(self, node: Node) -> Any: ...
        #   0: return 'bool' if node.id in ('True', 'False') else node.id
        #   0: return Any
    def do_Num(self, node: Node) -> str: ...
        #   0: return 'number'
        #   0: return str
    def do_Str(self, node: Node) -> str: ...
        #   0: return 'str'
        #   0: return str
class LeoGlobals:
    class NullObject:
        def __init__(self, *args, **keys) -> None: ...
        def __call__(self, *args, **keys) -> Any: ...
            #   0: return self
            # ? 0: return self
        def __repr__(self) -> str: ...
            #   0: return 'NullObject'
            #   0: return str
        def __str__(self) -> str: ...
            #   0: return 'NullObject'
            #   0: return str
        def __bool__(self) -> bool: ...
            #   0: return False
            #   0: return bool
        def __nonzero__(self) -> number: ...
            #   0: return 0
            #   0: return number
        def __delattr__(self, attr: Any) -> Any: ...
            #   0: return self
            # ? 0: return self
        def __getattr__(self, attr: Any) -> Any: ...
            #   0: return self
            # ? 0: return self
        def __setattr__(self, attr: Any, val: Any) -> Any: ...
            #   0: return self
            # ? 0: return self
    def _callerName(self, n: int=1, files: Any=False) -> str: ...
        #   0: return '%s:%s'%(self.shortFileName(code1.co_filename), name)
        #   0: return str
        #   1: return name
        #   1: return str
        #   2: return ''
        #   2: return str
        #   3: return ''
        #   3: return str
    def callers(self, n: int=4, count: Any=0, excludeCaller: Any=True, files: Any=False) -> str: ...
        #   0: return sep.join(result)
        #   0: return str
    def cls(self) -> None: ...
    def pdb(self) -> None: ...
    def shortFileName(self, fileName: Any, n: int=None) -> str: ...
        #   0: return os.path.basename(fileName)
        #   0: return str
        #   1: return '/'.join(fileName.replace('\\','/').split('/')[-n:])
        #   1: return str
    def splitLines(self, s: str) -> Any: ...
        #   0: return s.splitlines(True) if s else []
        #   0: return Any
    def trace(self, *args, **keys) -> None: ...
class Pattern(object):
    def __init__(self, find_s: str, repl_s: str='') -> None: ...
    def __eq__(self, obj: Any) -> bool: ...
        #   0: return self.find_s==obj.find_s and self.repl_s==obj.repl_s
        #   0: return bool
        #   1: return NotImplemented
        #   1: return bool
    def __ne__(self, obj: Any) -> bool: ...
        #   0: return  not self.__eq__(obj)
        #   0: return bool
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
        #   0: return '%s: %s'%(self.find_s, self.repl_s)
        #   0: return str
    def is_balanced(self) -> bool: ...
        #   0: return True
        #   0: return bool
        #   1: return True
        #   1: return bool
        #   2: return False
        #   2: return bool
    def is_regex(self) -> Any: ...
        #   0: return self.find_s.endswith('$')
        # ? 0: return self.find_s.endswith(str)
    def all_matches(self, s: str) -> Any: ...
        #   0: return aList
        #   0: return List[Any]
        #   1: return list(self.regex.finditer(s))
        # ? 1: return List[self.regex.finditer(str)]
    def full_balanced_match(self, s: str, i: int) -> Optional[int]: ...
        #   0: return i if found else None
        #   0: return Optional[int]
    def match_balanced(self, delim: Any, s: str, i: int) -> number: ...
        #   0: return i
        #   0: return int
        #   1: return len(s)+1
        #   1: return number
    def match(self, s: str, trace: bool=False) -> Tuple[bool, str]: ...
        #   0: return (False, s)
        #   0: return Tuple[bool, str]
        #   1: return (True, s)
        #   1: return Tuple[bool, str]
        #   2: return (True, s)
        #   2: return Tuple[bool, str]
        #   3: return (False, s)
        #   3: return Tuple[bool, str]
    def match_entire_string(self, s: str) -> Union[Any, bool]: ...
        #   0: return j is not None
        #   0: return bool
        #   1: return m and m.group(0)==s
        #   1: return Any
    def replace(self, m: Any, s: str) -> Any: ...
        #   0: return self.replace_balanced(s,start,end)
        # ? 0: return self.replace_balanced(str, start, end)
        #   1: return self.replace_regex(m,s)
        # ? 1: return self.replace_regex(m, str)
    def replace_balanced(self, s1: str, start: Any, end: Any) -> str: ...
        #   0: return s1[:start]+r+s1[end:]
        #   0: return str
        #   1: return s1[:start]+r+s1[end:]
        #   1: return str
        #   2: return s1[:start]+repl+s1[end:]
        #   2: return str
    def replace_regex(self, m: Any, s: str) -> str: ...
        #   0: return s
        #   0: return str
class StandAloneMakeStubFile:
    def __init__(self) -> None: ...
    def finalize(self, fn: str) -> str: ...
        #   0: return fn
        #   0: return str
    def make_stub_file(self, fn: str) -> None: ...
    def run(self) -> None: ...
    def run_all_unit_tests(self) -> None: ...
    def scan_command_line(self) -> None: ...
    def scan_options(self) -> None: ...
    def make_op_name_dict(self) -> Any: ...
        #   0: return d
        # ? 0: return d
    def create_parser(self) -> Any: ...
        #   0: return parser
        # ? 0: return optparse.OptionParser
    def find_pattern_ops(self, pattern: Any) -> Any: ...
        #   0: return []
        #   0: return List[]
        #   1: return ops
        # ? 1: return ops
    def get_config_string(self) -> str: ...
        #   0: return s
        #   0: return str
        #   1: return ''
        #   1: return str
    def init_parser(self, s: str) -> None: ...
    def is_section_name(self, s: str) -> Any: ...
        #   0: return s.strip().lower().replace(' ','')
        # ? 0: return str.strip().lower().replace(str, str)
        #   1: return True
        #   1: return bool
        #   2: return False
        #   2: return bool
        def munge(s: str) -> Any: ...
            #   0: return s.strip().lower().replace(' ','')
            # ? 0: return str.strip().lower().replace(str, str)
    def make_patterns_dict(self) -> None: ...
    def scan_patterns(self, section_name: Any) -> List[Any]: ...
        #   0: return aList
        #   0: return List[Any]
class Stub(object):
    def __init__(self, kind: Any, name: str, parent: Any=None, stack: Any=None) -> None: ...
    def __eq__(self, obj: Any) -> bool: ...
        #   0: return self.full_name==obj.full_name and self.kind==obj.kind
        #   0: return bool
        #   1: return NotImplemented
        #   1: return bool
    def __ne__(self, obj: Any) -> bool: ...
        #   0: return  not self.__eq__(obj)
        #   0: return bool
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
        #   0: return 'Stub: %s %s'%(id(self), self.full_name)
        #   0: return str
    def __str__(self) -> str: ...
        #   0: return 'Stub: %s'%self.full_name
        #   0: return str
    def level(self) -> int: ...
        #   0: return len(self.parents())
        #   0: return int
    def parents(self) -> Any: ...
        #   0: return self.full_name.split('.')[:-1]
        # ? 0: return self.full_name.split(str)[:number]
class StubFormatter(AstFormatter):
    def __init__(self, controller: StandAloneMakeStubFile, traverser: Any) -> None: ...
    def match_all(self, node: Node, s: str) -> str: ...
        #   0: return s
        #   0: return str
    def visit(self, node: Node) -> str: ...
        #   0: return s
        #   0: return str
    def trace_visitor(self, node: Node, op: Any, s: str) -> None: ...
    def do_Attribute(self, node: Node) -> str: ...
    def do_Bytes(self, node: Node) -> str: ...
    def do_Num(self, node: Node) -> str: ...
    def do_Str(self, node: Node) -> str: ...
    def do_Dict(self, node: Node) -> str: ...
    def do_List(self, node: Node) -> str: ...
    def do_Name(self, node: Node) -> str: ...
    def do_Tuple(self, node: Node) -> str: ...
    def do_BinOp(self, node: Node) -> str: ...
    def do_BoolOp(self, node: Node) -> str: ...
    def do_Call(self, node: Node) -> str: ...
    def do_keyword(self, node: Node) -> str: ...
    def do_Compare(self, node: Node) -> str: ...
    def do_IfExp(self, node: Node) -> str: ...
    def do_Subscript(self, node: Node) -> str: ...
    def do_UnaryOp(self, node: Node) -> str: ...
    def do_Return(self, node: Node) -> str: ...
class StubTraverser(ast.NodeVisitor):
    def __init__(self, controller: StandAloneMakeStubFile) -> None: ...
    def add_stub(self, d: Any, stub: Any) -> None: ...
    def indent(self, s: str) -> str: ...
        #   0: return '%s%s'%(' '*4*self.level, s)
        #   0: return str
    def out(self, s: str) -> None: ...
    def run(self, node: Node) -> None: ...
    def output_stubs(self, stub: Any) -> None: ...
    def output_time_stamp(self) -> None: ...
    def update(self, fn: str, new_root: Any) -> Any: ...
        #   0: return new_root
        # ? 0: return new_root
        #   1: return new_root
        # ? 1: return new_root
        #   2: return old_root
        # ? 2: return old_root
        #   3: return new_root
        # ? 3: return new_root
    def get_stub_file(self, fn: str) -> Optional[str]: ...
        #   0: return s
        #   0: return str
        #   1: return None
        #   1: return None
    def parse_stub_file(self, s: str, root_name: Any) -> Any: ...
        #   0: return (d, root)
        # ? 0: return Tuple[d, root]
    def merge_stubs(self, new_stubs: Any, old_root: Any, new_root: Any, trace: bool=False) -> None: ...
    def check_delete(self, new_stubs: Any, old_root: Any, new_root: Any, trace: bool) -> Any: ...
        #   0: return delete_list
        # ? 0: return delete_list
    def flatten_stubs(self, root: Any) -> List[Any]: ...
        #   0: return aList
        #   0: return List[Any]
    def flatten_stubs_helper(self, root: Any, aList: List[Any]) -> None: ...
    def find_parent_stub(self, stub: Any, root: Any) -> Any: ...
        #   0: return self.find_stub(stub.parent,root) if stub.parent else None
        #   0: return Any
    def find_stub(self, stub: Any, root: Any) -> Any: ...
        #   0: return root
        # ? 0: return root
        #   1: return stub2
        # ? 1: return stub2
        #   2: return None
        #   2: return None
    def sort_stubs_by_hierarchy(self, stubs1: Any) -> Any: ...
        #   0: return result
        # ? 0: return result
        #   1: return []
        #   1: return List[]
    def trace_stubs(self, stub: Any, aList: List[Any]=None, header: Any=None, level: Any=-1) -> str: ...
        #   0: return '\n'.join(aList)+'\n'
        #   0: return str
    def visit_ClassDef(self, node: Node) -> None: ...
    def visit_FunctionDef(self, node: Node) -> None: ...
    def format_arguments(self, node: Node) -> str: ...
        #   0: return ', '.join(result)
        #   0: return str
    def munge_arg(self, s: str) -> str: ...
        #   0: return s
        #   0: return str
        #   1: return '%s: %s'%(s, pattern.repl_s)
        #   1: return str
        #   2: return s+': Any'
        #   2: return str
    def format_returns(self, node: Node) -> Any: ...
        #   0: return 'None: ...'
        #   0: return str
        #   1: return s+': ...'
        #   1: return str
        #   2: return self.format_return_expressions(name,raw,r)
        # ? 2: return self.format_return_expressions(str, raw, r)
    def format_return_expressions(self, name: str, raw_returns: Any, reduced_returns: Any) -> str: ...
        #   0: return s+': ...'+results
        #   0: return str
        #   1: return 'Any: ...'+results
        #   1: return str
        #   2: return s+': ...'
        #   2: return str
    def get_def_name(self, node: Node) -> str: ...
        #   0: return name
        #   0: return str
    def remove_recursive_calls(self, name: str, raw: Any, reduced: Any) -> Any: ...
        #   0: return (raw_result, reduced_result)
        # ? 0: return Tuple[raw_result, reduced_result]
    def visit_Return(self, node: Node) -> None: ...
class TestClass:
    def parse_group(group: str) -> Tuple[int, str]: ...
        #   0: return (ndots, os.sep.join(group[::2]))
        #   0: return Tuple[int, str]
    def return_all(self) -> bool: ...
        #   0: return all(is_known_type(z) for z in s3.split(','))
        #   0: return bool
    def return_array() -> Any: ...
        #   0: return f(s[1:-1])
        # ? 0: return f(str)
    def return_list(self, a: str) -> List[str]: ...
        #   0: return [a]
        #   0: return List[str]
    def return_two_lists(s: str) -> Any: ...
        #   0: return aList
        #   0: return List[Any]
        #   1: return list(self.regex.finditer(s))
        # ? 1: return List[self.regex.finditer(str)]
