(() => {
  var __create = Object.create;
  var __defProp = Object.defineProperty;
  var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
  var __getOwnPropNames = Object.getOwnPropertyNames;
  var __getProtoOf = Object.getPrototypeOf;
  var __hasOwnProp = Object.prototype.hasOwnProperty;
  var __commonJS = (cb, mod) => function __require() {
    try {
      return mod || (0, cb[__getOwnPropNames(cb)[0]])((mod = { exports: {} }).exports, mod), mod.exports;
    } catch (e2) {
      throw mod = 0, e2;
    }
  };
  var __copyProps = (to, from, except, desc) => {
    if (from && typeof from === "object" || typeof from === "function") {
      for (let key of __getOwnPropNames(from))
        if (!__hasOwnProp.call(to, key) && key !== except)
          __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
    }
    return to;
  };
  var __toESM = (mod, isNodeMode, target) => (target = mod != null ? __create(__getProtoOf(mod)) : {}, __copyProps(
    // If the importer is in node compatibility mode or this is not an ESM
    // file that has been converted to a CommonJS file using a Babel-
    // compatible transform (i.e. "__esModule" has not been set), then set
    // "default" to the CommonJS "module.exports" for node compatibility.
    isNodeMode || !mod || !mod.__esModule ? __defProp(target, "default", { value: mod, enumerable: true }) : target,
    mod
  ));

  // ../../node_modules/randomcolor/randomColor.js
  var require_randomColor = __commonJS({
    "../../node_modules/randomcolor/randomColor.js"(exports, module) {
      (function(root, factory) {
        if (typeof exports === "object") {
          var randomColor2 = factory();
          if (typeof module === "object" && module && module.exports) {
            exports = module.exports = randomColor2;
          }
          exports.randomColor = randomColor2;
        } else if (typeof define === "function" && define.amd) {
          define([], factory);
        } else {
          root.randomColor = factory();
        }
      })(exports, function() {
        var seed = null;
        var colorDictionary = {};
        loadColorBounds();
        var colorRanges = [];
        var randomColor2 = function(options) {
          options = options || {};
          if (options.seed !== void 0 && options.seed !== null && options.seed === parseInt(options.seed, 10)) {
            seed = options.seed;
          } else if (typeof options.seed === "string") {
            seed = stringToInteger(options.seed);
          } else if (options.seed !== void 0 && options.seed !== null) {
            throw new TypeError("The seed value must be an integer or string");
          } else {
            seed = null;
          }
          var H, S, B;
          if (options.count !== null && options.count !== void 0) {
            var totalColors = options.count, colors = [];
            for (var i = 0; i < options.count; i++) {
              colorRanges.push(false);
            }
            options.count = null;
            while (totalColors > colors.length) {
              var color = randomColor2(options);
              if (seed !== null) {
                options.seed = seed;
              }
              colors.push(color);
            }
            options.count = totalColors;
            return colors;
          }
          H = pickHue(options);
          S = pickSaturation(H, options);
          B = pickBrightness(H, S, options);
          return setFormat([H, S, B], options);
        };
        function pickHue(options) {
          if (colorRanges.length > 0) {
            var hueRange = getRealHueRange(options.hue);
            var hue = randomWithin(hueRange);
            var step = (hueRange[1] - hueRange[0]) / colorRanges.length;
            var j = parseInt((hue - hueRange[0]) / step);
            if (colorRanges[j] === true) {
              j = (j + 2) % colorRanges.length;
            } else {
              colorRanges[j] = true;
            }
            var min = (hueRange[0] + j * step) % 359, max = (hueRange[0] + (j + 1) * step) % 359;
            hueRange = [min, max];
            hue = randomWithin(hueRange);
            if (hue < 0) {
              hue = 360 + hue;
            }
            return hue;
          } else {
            var hueRange = getHueRange(options.hue);
            hue = randomWithin(hueRange);
            if (hue < 0) {
              hue = 360 + hue;
            }
            return hue;
          }
        }
        function pickSaturation(hue, options) {
          if (options.hue === "monochrome") {
            return 0;
          }
          if (options.luminosity === "random") {
            return randomWithin([0, 100]);
          }
          var saturationRange = getSaturationRange(hue);
          var sMin = saturationRange[0], sMax = saturationRange[1];
          switch (options.luminosity) {
            case "bright":
              sMin = 55;
              break;
            case "dark":
              sMin = sMax - 10;
              break;
            case "light":
              sMax = 55;
              break;
          }
          return randomWithin([sMin, sMax]);
        }
        function pickBrightness(H, S, options) {
          var bMin = getMinimumBrightness(H, S), bMax = 100;
          switch (options.luminosity) {
            case "dark":
              bMax = bMin + 20;
              break;
            case "light":
              bMin = (bMax + bMin) / 2;
              break;
            case "random":
              bMin = 0;
              bMax = 100;
              break;
          }
          return randomWithin([bMin, bMax]);
        }
        function setFormat(hsv, options) {
          switch (options.format) {
            case "hsvArray":
              return hsv;
            case "hslArray":
              return HSVtoHSL(hsv);
            case "hsl":
              var hsl = HSVtoHSL(hsv);
              return "hsl(" + hsl[0] + ", " + hsl[1] + "%, " + hsl[2] + "%)";
            case "hsla":
              var hslColor = HSVtoHSL(hsv);
              var alpha = options.alpha || Math.random();
              return "hsla(" + hslColor[0] + ", " + hslColor[1] + "%, " + hslColor[2] + "%, " + alpha + ")";
            case "rgbArray":
              return HSVtoRGB(hsv);
            case "rgb":
              var rgb = HSVtoRGB(hsv);
              return "rgb(" + rgb.join(", ") + ")";
            case "rgba":
              var rgbColor = HSVtoRGB(hsv);
              var alpha = options.alpha || Math.random();
              return "rgba(" + rgbColor.join(", ") + ", " + alpha + ")";
            default:
              return HSVtoHex(hsv);
          }
        }
        function getMinimumBrightness(H, S) {
          var lowerBounds = getColorInfo(H).lowerBounds;
          for (var i = 0; i < lowerBounds.length - 1; i++) {
            var s1 = lowerBounds[i][0], v1 = lowerBounds[i][1];
            var s2 = lowerBounds[i + 1][0], v2 = lowerBounds[i + 1][1];
            if (S >= s1 && S <= s2) {
              var m = (v2 - v1) / (s2 - s1), b = v1 - m * s1;
              return m * S + b;
            }
          }
          return 0;
        }
        function getHueRange(colorInput) {
          if (typeof parseInt(colorInput) === "number") {
            var number = parseInt(colorInput);
            if (number < 360 && number > 0) {
              return [number, number];
            }
          }
          if (typeof colorInput === "string") {
            if (colorDictionary[colorInput]) {
              var color = colorDictionary[colorInput];
              if (color.hueRange) {
                return color.hueRange;
              }
            } else if (colorInput.match(/^#?([0-9A-F]{3}|[0-9A-F]{6})$/i)) {
              var hue = HexToHSB(colorInput)[0];
              return [hue, hue];
            }
          }
          return [0, 360];
        }
        function getSaturationRange(hue) {
          return getColorInfo(hue).saturationRange;
        }
        function getColorInfo(hue) {
          if (hue >= 334 && hue <= 360) {
            hue -= 360;
          }
          for (var colorName in colorDictionary) {
            var color = colorDictionary[colorName];
            if (color.hueRange && hue >= color.hueRange[0] && hue <= color.hueRange[1]) {
              return colorDictionary[colorName];
            }
          }
          return "Color not found";
        }
        function randomWithin(range) {
          if (seed === null) {
            var golden_ratio = 0.618033988749895;
            var r = Math.random();
            r += golden_ratio;
            r %= 1;
            return Math.floor(range[0] + r * (range[1] + 1 - range[0]));
          } else {
            var max = range[1] || 1;
            var min = range[0] || 0;
            seed = (seed * 9301 + 49297) % 233280;
            var rnd = seed / 233280;
            return Math.floor(min + rnd * (max - min));
          }
        }
        function HSVtoHex(hsv) {
          var rgb = HSVtoRGB(hsv);
          function componentToHex(c) {
            var hex2 = c.toString(16);
            return hex2.length == 1 ? "0" + hex2 : hex2;
          }
          var hex = "#" + componentToHex(rgb[0]) + componentToHex(rgb[1]) + componentToHex(rgb[2]);
          return hex;
        }
        function defineColor(name, hueRange, lowerBounds) {
          var sMin = lowerBounds[0][0], sMax = lowerBounds[lowerBounds.length - 1][0], bMin = lowerBounds[lowerBounds.length - 1][1], bMax = lowerBounds[0][1];
          colorDictionary[name] = {
            hueRange,
            lowerBounds,
            saturationRange: [sMin, sMax],
            brightnessRange: [bMin, bMax]
          };
        }
        function loadColorBounds() {
          defineColor(
            "monochrome",
            null,
            [[0, 0], [100, 0]]
          );
          defineColor(
            "red",
            [-26, 18],
            [[20, 100], [30, 92], [40, 89], [50, 85], [60, 78], [70, 70], [80, 60], [90, 55], [100, 50]]
          );
          defineColor(
            "orange",
            [18, 46],
            [[20, 100], [30, 93], [40, 88], [50, 86], [60, 85], [70, 70], [100, 70]]
          );
          defineColor(
            "yellow",
            [46, 62],
            [[25, 100], [40, 94], [50, 89], [60, 86], [70, 84], [80, 82], [90, 80], [100, 75]]
          );
          defineColor(
            "green",
            [62, 178],
            [[30, 100], [40, 90], [50, 85], [60, 81], [70, 74], [80, 64], [90, 50], [100, 40]]
          );
          defineColor(
            "blue",
            [178, 257],
            [[20, 100], [30, 86], [40, 80], [50, 74], [60, 60], [70, 52], [80, 44], [90, 39], [100, 35]]
          );
          defineColor(
            "purple",
            [257, 282],
            [[20, 100], [30, 87], [40, 79], [50, 70], [60, 65], [70, 59], [80, 52], [90, 45], [100, 42]]
          );
          defineColor(
            "pink",
            [282, 334],
            [[20, 100], [30, 90], [40, 86], [60, 84], [80, 80], [90, 75], [100, 73]]
          );
        }
        function HSVtoRGB(hsv) {
          var h = hsv[0];
          if (h === 0) {
            h = 1;
          }
          if (h === 360) {
            h = 359;
          }
          h = h / 360;
          var s = hsv[1] / 100, v = hsv[2] / 100;
          var h_i = Math.floor(h * 6), f = h * 6 - h_i, p = v * (1 - s), q = v * (1 - f * s), t = v * (1 - (1 - f) * s), r = 256, g = 256, b = 256;
          switch (h_i) {
            case 0:
              r = v;
              g = t;
              b = p;
              break;
            case 1:
              r = q;
              g = v;
              b = p;
              break;
            case 2:
              r = p;
              g = v;
              b = t;
              break;
            case 3:
              r = p;
              g = q;
              b = v;
              break;
            case 4:
              r = t;
              g = p;
              b = v;
              break;
            case 5:
              r = v;
              g = p;
              b = q;
              break;
          }
          var result = [Math.floor(r * 255), Math.floor(g * 255), Math.floor(b * 255)];
          return result;
        }
        function HexToHSB(hex) {
          hex = hex.replace(/^#/, "");
          hex = hex.length === 3 ? hex.replace(/(.)/g, "$1$1") : hex;
          var red = parseInt(hex.substr(0, 2), 16) / 255, green = parseInt(hex.substr(2, 2), 16) / 255, blue = parseInt(hex.substr(4, 2), 16) / 255;
          var cMax = Math.max(red, green, blue), delta = cMax - Math.min(red, green, blue), saturation = cMax ? delta / cMax : 0;
          switch (cMax) {
            case red:
              return [60 * ((green - blue) / delta % 6) || 0, saturation, cMax];
            case green:
              return [60 * ((blue - red) / delta + 2) || 0, saturation, cMax];
            case blue:
              return [60 * ((red - green) / delta + 4) || 0, saturation, cMax];
          }
        }
        function HSVtoHSL(hsv) {
          var h = hsv[0], s = hsv[1] / 100, v = hsv[2] / 100, k = (2 - s) * v;
          return [
            h,
            Math.round(s * v / (k < 1 ? k : 2 - k) * 1e4) / 100,
            k / 2 * 100
          ];
        }
        function stringToInteger(string) {
          var total = 0;
          for (var i = 0; i !== string.length; i++) {
            if (total >= Number.MAX_SAFE_INTEGER) break;
            total += string.charCodeAt(i);
          }
          return total;
        }
        function getRealHueRange(colorHue) {
          if (!isNaN(colorHue)) {
            var number = parseInt(colorHue);
            if (number < 360 && number > 0) {
              return getColorInfo(colorHue).hueRange;
            }
          } else if (typeof colorHue === "string") {
            if (colorDictionary[colorHue]) {
              var color = colorDictionary[colorHue];
              if (color.hueRange) {
                return color.hueRange;
              }
            } else if (colorHue.match(/^#?([0-9A-F]{3}|[0-9A-F]{6})$/i)) {
              var hue = HexToHSB(colorHue)[0];
              return getColorInfo(hue).hueRange;
            }
          }
          return [0, 360];
        }
        return randomColor2;
      });
    }
  });

  // ../../node_modules/min-dash/dist/index.js
  var nativeToString = Object.prototype.toString;
  var nativeHasOwnProperty = Object.prototype.hasOwnProperty;
  function isUndefined(obj) {
    return obj === void 0;
  }
  function isNil(obj) {
    return obj == null;
  }
  function isArray(obj) {
    return nativeToString.call(obj) === "[object Array]";
  }
  function isFunction(obj) {
    const tag = nativeToString.call(obj);
    return tag === "[object Function]" || tag === "[object AsyncFunction]" || tag === "[object GeneratorFunction]" || tag === "[object AsyncGeneratorFunction]" || tag === "[object Proxy]";
  }
  function has(target, key) {
    return !isNil(target) && nativeHasOwnProperty.call(target, key);
  }
  function find(collection, matcher) {
    const matchFn = toMatcher(matcher);
    let match;
    forEach(collection, function(val, key) {
      if (matchFn(val, key)) {
        match = val;
        return false;
      }
    });
    return match;
  }
  function forEach(collection, iterator) {
    let val, result;
    if (isUndefined(collection)) {
      return;
    }
    const convertKey = isArray(collection) ? toNum : identity;
    for (let key in collection) {
      if (has(collection, key)) {
        val = collection[key];
        result = iterator(val, convertKey(key));
        if (result === false) {
          return val;
        }
      }
    }
  }
  function some(collection, matcher) {
    return !!find(collection, matcher);
  }
  function toMatcher(matcher) {
    return isFunction(matcher) ? matcher : (e2) => {
      return e2 === matcher;
    };
  }
  function identity(arg) {
    return arg;
  }
  function toNum(arg) {
    return Number(arg);
  }

  // ../../node_modules/domify/index.js
  var wrapMap = {
    legend: [1, "<fieldset>", "</fieldset>"],
    tr: [2, "<table><tbody>", "</tbody></table>"],
    col: [2, "<table><tbody></tbody><colgroup>", "</colgroup></table>"],
    _default: [0, "", ""]
  };
  wrapMap.td = wrapMap.th = [3, "<table><tbody><tr>", "</tr></tbody></table>"];
  wrapMap.option = wrapMap.optgroup = [1, '<select multiple="multiple">', "</select>"];
  wrapMap.thead = wrapMap.tbody = wrapMap.colgroup = wrapMap.caption = wrapMap.tfoot = [1, "<table>", "</table>"];
  wrapMap.polyline = wrapMap.ellipse = wrapMap.polygon = wrapMap.circle = wrapMap.text = wrapMap.line = wrapMap.path = wrapMap.rect = wrapMap.g = [1, '<svg xmlns="http://www.w3.org/2000/svg" version="1.1">', "</svg>"];
  function domify(htmlString, document2 = globalThis.document) {
    if (typeof htmlString !== "string") {
      throw new TypeError("String expected");
    }
    const commentMatch = /^<!--(.*?)-->$/s.exec(htmlString);
    if (commentMatch) {
      return document2.createComment(commentMatch[1]);
    }
    const tagName = /<([\w:]+)/.exec(htmlString)?.[1];
    if (!tagName) {
      return document2.createTextNode(htmlString);
    }
    htmlString = htmlString.trim();
    if (tagName === "body") {
      const element2 = document2.createElement("html");
      element2.innerHTML = htmlString;
      const { lastChild } = element2;
      lastChild.remove();
      return lastChild;
    }
    let [depth, prefix, suffix] = Object.hasOwn(wrapMap, tagName) ? wrapMap[tagName] : wrapMap._default;
    let element = document2.createElement("div");
    element.innerHTML = prefix + htmlString + suffix;
    while (depth--) {
      element = element.lastChild;
    }
    if (element.firstChild === element.lastChild) {
      const { firstChild } = element;
      firstChild.remove();
      return firstChild;
    }
    const fragment = document2.createDocumentFragment();
    fragment.append(...element.childNodes);
    return fragment;
  }

  // ../../node_modules/min-dom/dist/index.js
  function _mergeNamespaces(n, m) {
    m.forEach(function(e2) {
      e2 && typeof e2 !== "string" && !Array.isArray(e2) && Object.keys(e2).forEach(function(k) {
        if (k !== "default" && !(k in n)) {
          var d = Object.getOwnPropertyDescriptor(e2, k);
          Object.defineProperty(n, k, d.get ? d : {
            enumerable: true,
            get: function() {
              return e2[k];
            }
          });
        }
      });
    });
    return Object.freeze(n);
  }
  var toString = Object.prototype.toString;
  function classes(el) {
    return new ClassList(el);
  }
  function ClassList(el) {
    if (!el || !el.nodeType) {
      throw new Error("A DOM element reference is required");
    }
    this.el = el;
    this.list = el.classList;
  }
  ClassList.prototype.add = function(name) {
    this.list.add(name);
    return this;
  };
  ClassList.prototype.remove = function(name) {
    if ("[object RegExp]" == toString.call(name)) {
      return this.removeMatching(name);
    }
    this.list.remove(name);
    return this;
  };
  ClassList.prototype.removeMatching = function(re) {
    const arr = this.array();
    for (let i = 0; i < arr.length; i++) {
      if (re.test(arr[i])) {
        this.remove(arr[i]);
      }
    }
    return this;
  };
  ClassList.prototype.toggle = function(name, force) {
    if ("undefined" !== typeof force) {
      if (force !== this.list.toggle(name, force)) {
        this.list.toggle(name);
      }
    } else {
      this.list.toggle(name);
    }
    return this;
  };
  ClassList.prototype.array = function() {
    return Array.from(this.list);
  };
  ClassList.prototype.has = ClassList.prototype.contains = function(name) {
    return this.list.contains(name);
  };
  function clear(element) {
    var child;
    while (child = element.firstChild) {
      element.removeChild(child);
    }
    return element;
  }
  function closest(element, selector, checkYourSelf) {
    var actualElement = checkYourSelf ? element : element.parentNode;
    return actualElement && typeof actualElement.closest === "function" && actualElement.closest(selector) || null;
  }
  function getDefaultExportFromCjs(x) {
    return x && x.__esModule && Object.prototype.hasOwnProperty.call(x, "default") ? x["default"] : x;
  }
  var componentEvent = {};
  var hasRequiredComponentEvent;
  function requireComponentEvent() {
    if (hasRequiredComponentEvent) return componentEvent;
    hasRequiredComponentEvent = 1;
    var bind2, unbind2, prefix;
    function detect() {
      bind2 = window.addEventListener ? "addEventListener" : "attachEvent";
      unbind2 = window.removeEventListener ? "removeEventListener" : "detachEvent";
      prefix = bind2 !== "addEventListener" ? "on" : "";
    }
    componentEvent.bind = function(el, type, fn, capture) {
      if (!bind2) detect();
      el[bind2](prefix + type, fn, capture || false);
      return fn;
    };
    componentEvent.unbind = function(el, type, fn, capture) {
      if (!unbind2) detect();
      el[unbind2](prefix + type, fn, capture || false);
      return fn;
    };
    return componentEvent;
  }
  var componentEventExports = requireComponentEvent();
  var index = /* @__PURE__ */ getDefaultExportFromCjs(componentEventExports);
  var event = /* @__PURE__ */ _mergeNamespaces({
    __proto__: null,
    default: index
  }, [componentEventExports]);
  var forceCaptureEvents = ["focus", "blur"];
  function bind(el, selector, type, fn, capture) {
    if (forceCaptureEvents.indexOf(type) !== -1) {
      capture = true;
    }
    return event.bind(el, type, function(e2) {
      var target = e2.target || e2.srcElement;
      e2.delegateTarget = closest(target, selector, true);
      if (e2.delegateTarget) {
        fn.call(el, e2);
      }
    }, capture);
  }
  function unbind(el, type, fn, capture) {
    if (forceCaptureEvents.indexOf(type) !== -1) {
      capture = true;
    }
    return event.unbind(el, type, fn, capture);
  }
  var delegate = {
    bind,
    unbind
  };
  function query(selector, el) {
    el = el || document;
    return el.querySelector(selector);
  }
  function all(selector, el) {
    el = el || document;
    return el.querySelectorAll(selector);
  }

  // ../../node_modules/bpmn-js-token-simulation/lib/util/EventHelper.js
  var TOGGLE_MODE_EVENT = "tokenSimulation.toggleMode";
  var PLAY_SIMULATION_EVENT = "tokenSimulation.playSimulation";
  var PAUSE_SIMULATION_EVENT = "tokenSimulation.pauseSimulation";
  var RESET_SIMULATION_EVENT = "tokenSimulation.resetSimulation";
  var ANIMATION_CREATED_EVENT = "tokenSimulation.animationCreated";
  var ANIMATION_SPEED_CHANGED_EVENT = "tokenSimulation.animationSpeedChanged";
  var ELEMENT_CHANGED_EVENT = "tokenSimulation.simulator.elementChanged";
  var SCOPE_DESTROYED_EVENT = "tokenSimulation.simulator.destroyScope";
  var SCOPE_CHANGED_EVENT = "tokenSimulation.simulator.scopeChanged";
  var SCOPE_CREATE_EVENT = "tokenSimulation.simulator.createScope";
  var SCOPE_FILTER_CHANGED_EVENT = "tokenSimulation.scopeFilterChanged";
  var TRACE_EVENT = "tokenSimulation.simulator.trace";

  // ../../node_modules/bpmn-js-token-simulation/lib/icons/index.js
  var LogSVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!-- Font Awesome Free 5.15.4 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) --><path fill="currentColor" d="M12.83 352h262.34A12.82 12.82 0 0 0 288 339.17v-38.34A12.82 12.82 0 0 0 275.17 288H12.83A12.82 12.82 0 0 0 0 300.83v38.34A12.82 12.82 0 0 0 12.83 352zm0-256h262.34A12.82 12.82 0 0 0 288 83.17V44.83A12.82 12.82 0 0 0 275.17 32H12.83A12.82 12.82 0 0 0 0 44.83v38.34A12.82 12.82 0 0 0 12.83 96zM432 160H16a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h416a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm0 256H16a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h416a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16z"/></svg>';
  var AngleRightSVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 512"><!-- Font Awesome Free 5.15.4 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) --><path fill="currentColor" d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"/></svg>';
  var CheckCircleSVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!-- Font Awesome Free 5.15.4 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) --><path fill="currentColor" d="M504 256c0 136.967-111.033 248-248 248S8 392.967 8 256 119.033 8 256 8s248 111.033 248 248zM227.314 387.314l184-184c6.248-6.248 6.248-16.379 0-22.627l-22.627-22.627c-6.248-6.249-16.379-6.249-22.628 0L216 308.118l-70.059-70.059c-6.248-6.248-16.379-6.248-22.628 0l-22.627 22.627c-6.248 6.248-6.248 16.379 0 22.627l104 104c6.249 6.249 16.379 6.249 22.628.001z"/></svg>';
  var ForkSVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><!-- Font Awesome Free 5.15.4 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) --><path fill="currentColor" d="M384 144c0-44.2-35.8-80-80-80s-80 35.8-80 80c0 36.4 24.3 67.1 57.5 76.8-.6 16.1-4.2 28.5-11 36.9-15.4 19.2-49.3 22.4-85.2 25.7-28.2 2.6-57.4 5.4-81.3 16.9v-144c32.5-10.2 56-40.5 56-76.3 0-44.2-35.8-80-80-80S0 35.8 0 80c0 35.8 23.5 66.1 56 76.3v199.3C23.5 365.9 0 396.2 0 432c0 44.2 35.8 80 80 80s80-35.8 80-80c0-34-21.2-63.1-51.2-74.6 3.1-5.2 7.8-9.8 14.9-13.4 16.2-8.2 40.4-10.4 66.1-12.8 42.2-3.9 90-8.4 118.2-43.4 14-17.4 21.1-39.8 21.6-67.9 31.6-10.8 54.4-40.7 54.4-75.9zM80 64c8.8 0 16 7.2 16 16s-7.2 16-16 16-16-7.2-16-16 7.2-16 16-16zm0 384c-8.8 0-16-7.2-16-16s7.2-16 16-16 16 7.2 16 16-7.2 16-16 16zm224-320c8.8 0 16 7.2 16 16s-7.2 16-16 16-16-7.2-16-16 7.2-16 16-16z"/></svg>';
  var ExclamationTriangleSVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><!-- Font Awesome Free 5.15.4 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) --><path fill="currentColor" d="M569.517 440.013C587.975 472.007 564.806 512 527.94 512H48.054c-36.937 0-59.999-40.055-41.577-71.987L246.423 23.985c18.467-32.009 64.72-31.951 83.154 0l239.94 416.028zM288 354c-25.405 0-46 20.595-46 46s20.595 46 46 46 46-20.595 46-46-20.595-46-46-46zm-43.673-165.346l7.418 136c.347 6.364 5.609 11.346 11.982 11.346h48.546c6.373 0 11.635-4.982 11.982-11.346l7.418-136c.375-6.874-5.098-12.654-11.982-12.654h-63.383c-6.884 0-12.356 5.78-11.981 12.654z"/></svg>';
  var InfoSVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 192 512"><!-- Font Awesome Free 5.15.4 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) --><path fill="currentColor" d="M20 424.229h20V279.771H20c-11.046 0-20-8.954-20-20V212c0-11.046 8.954-20 20-20h112c11.046 0 20 8.954 20 20v212.229h20c11.046 0 20 8.954 20 20V492c0 11.046-8.954 20-20 20H20c-11.046 0-20-8.954-20-20v-47.771c0-11.046 8.954-20 20-20zM96 0C56.235 0 24 32.235 24 72s32.235 72 72 72 72-32.235 72-72S135.764 0 96 0z"/></svg>';
  var PauseSVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!-- Font Awesome Free 5.15.4 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) --><path fill="currentColor" d="M144 479H48c-26.5 0-48-21.5-48-48V79c0-26.5 21.5-48 48-48h96c26.5 0 48 21.5 48 48v352c0 26.5-21.5 48-48 48zm304-48V79c0-26.5-21.5-48-48-48h-96c-26.5 0-48 21.5-48 48v352c0 26.5 21.5 48 48 48h96c26.5 0 48-21.5 48-48z"/></svg>';
  var RemovePauseSVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580.5 448">\n  <path fill="currentColor" d="M112 0C85 0 64 22 64 48v196l192-89V48c0-26-22-48-48-48zm256 0c-27 0-48 22-48 48v77l190-89c-5-21-24-36-46-36Zm144 105-192 89v70l192-89zM256 224 64 314v70l192-90zm256 21-192 89v66c0 27 21 48 48 48h96c26 0 48-21 48-48zM256 364 89 442c7 4 14 6 23 6h96c26 0 48-21 48-48z"/>\n  <rect fill="currentColor" width="63.3" height="618.2" x="311.5" y="-469.4" transform="rotate(65)" rx="10"/>\n</svg>\n';
  var PlaySVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!-- Adapted from Font Awesome Free 5.15.4 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) --><path fill="currentColor" d="M424.4 214.7L72.4 6.6C43.8-10.3 0 6.1 0 47.9V464c0 37.5 40.7 60.1 72.4 41.3l352-208c31.4-18.5 31.5-64.1 0-82.6z"/></svg>';
  var ResetSVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!-- Font Awesome Free 5.15.4 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) --><path fill="currentColor" d="M440.65 12.57l4 82.77A247.16 247.16 0 0 0 255.83 8C134.73 8 33.91 94.92 12.29 209.82A12 12 0 0 0 24.09 224h49.05a12 12 0 0 0 11.67-9.26 175.91 175.91 0 0 1 317-56.94l-101.46-4.86a12 12 0 0 0-12.57 12v47.41a12 12 0 0 0 12 12H500a12 12 0 0 0 12-12V12a12 12 0 0 0-12-12h-47.37a12 12 0 0 0-11.98 12.57zM255.83 432a175.61 175.61 0 0 1-146-77.8l101.8 4.87a12 12 0 0 0 12.57-12v-47.4a12 12 0 0 0-12-12H12a12 12 0 0 0-12 12V500a12 12 0 0 0 12 12h47.35a12 12 0 0 0 12-12.6l-4.15-82.57A247.17 247.17 0 0 0 255.83 504c121.11 0 221.93-86.92 243.55-201.82a12 12 0 0 0-11.8-14.18h-49.05a12 12 0 0 0-11.67 9.26A175.86 175.86 0 0 1 255.83 432z"/></svg>';
  var TachometerSVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><!-- Font Awesome Free 5.15.4 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) --><path fill="currentColor" d="M288 32C128.94 32 0 160.94 0 320c0 52.8 14.25 102.26 39.06 144.8 5.61 9.62 16.3 15.2 27.44 15.2h443c11.14 0 21.83-5.58 27.44-15.2C561.75 422.26 576 372.8 576 320c0-159.06-128.94-288-288-288zm0 64c14.71 0 26.58 10.13 30.32 23.65-1.11 2.26-2.64 4.23-3.45 6.67l-9.22 27.67c-5.13 3.49-10.97 6.01-17.64 6.01-17.67 0-32-14.33-32-32S270.33 96 288 96zM96 384c-17.67 0-32-14.33-32-32s14.33-32 32-32 32 14.33 32 32-14.33 32-32 32zm48-160c-17.67 0-32-14.33-32-32s14.33-32 32-32 32 14.33 32 32-14.33 32-32 32zm246.77-72.41l-61.33 184C343.13 347.33 352 364.54 352 384c0 11.72-3.38 22.55-8.88 32H232.88c-5.5-9.45-8.88-20.28-8.88-32 0-33.94 26.5-61.43 59.9-63.59l61.34-184.01c4.17-12.56 17.73-19.45 30.36-15.17 12.57 4.19 19.35 17.79 15.17 30.36zm14.66 57.2l15.52-46.55c3.47-1.29 7.13-2.23 11.05-2.23 17.67 0 32 14.33 32 32s-14.33 32-32 32c-11.38-.01-20.89-6.28-26.57-15.22zM480 384c-17.67 0-32-14.33-32-32s14.33-32 32-32 32 14.33 32 32-14.33 32-32 32z"/></svg>';
  var TimesCircleSVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!-- Font Awesome Free 5.15.4 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) --><path fill="currentColor" d="M256 8C119 8 8 119 8 256s111 248 248 248 248-111 248-248S393 8 256 8zm121.6 313.1c4.7 4.7 4.7 12.3 0 17L338 377.6c-4.7 4.7-12.3 4.7-17 0L256 312l-65.1 65.6c-4.7 4.7-12.3 4.7-17 0L134.4 338c-4.7-4.7-4.7-12.3 0-17l65.6-65-65.6-65.1c-4.7-4.7-4.7-12.3 0-17l39.6-39.6c4.7-4.7 12.3-4.7 17 0l65 65.7 65.1-65.6c4.7-4.7 12.3-4.7 17 0l39.6 39.6c4.7 4.7 4.7 12.3 0 17L312 256l65.6 65.1z"/></svg>';
  var TimesSVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 352 512"><!-- Font Awesome Free 5.15.4 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) --><path fill="currentColor" d="M242.72 256l100.07-100.07c12.28-12.28 12.28-32.19 0-44.48l-22.24-22.24c-12.28-12.28-32.19-12.28-44.48 0L176 189.28 75.93 89.21c-12.28-12.28-32.19-12.28-44.48 0L9.21 111.45c-12.28 12.28-12.28 32.19 0 44.48L109.28 256 9.21 356.07c-12.28 12.28-12.28 32.19 0 44.48l22.24 22.24c12.28 12.28 32.2 12.28 44.48 0L176 322.72l100.07 100.07c12.28 12.28 32.2 12.28 44.48 0l22.24-22.24c12.28-12.28 12.28-32.19 0-44.48L242.72 256z"/></svg>';
  var ToggleOffSVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><!-- Font Awesome Free 5.15.4 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) --><path fill="currentColor" d="M384 64H192C85.961 64 0 149.961 0 256s85.961 192 192 192h192c106.039 0 192-85.961 192-192S490.039 64 384 64zM64 256c0-70.741 57.249-128 128-128 70.741 0 128 57.249 128 128 0 70.741-57.249 128-128 128-70.741 0-128-57.249-128-128zm320 128h-48.905c65.217-72.858 65.236-183.12 0-256H384c70.741 0 128 57.249 128 128 0 70.74-57.249 128-128 128z"/></svg>';
  var ToggleOnSVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><!-- Font Awesome Free 5.15.4 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) --><path fill="currentColor" d="M384 64H192C86 64 0 150 0 256s86 192 192 192h192c106 0 192-86 192-192S490 64 384 64zm0 320c-70.8 0-128-57.3-128-128 0-70.8 57.3-128 128-128 70.8 0 128 57.3 128 128 0 70.8-57.3 128-128 128z"/></svg>';
  function createIcon(svg) {
    return function Icon(className = "") {
      return `<span class="bts-icon ${className}">${svg}</span>`;
    };
  }
  var LogIcon = createIcon(LogSVG);
  var AngleRightIcon = createIcon(AngleRightSVG);
  var CheckCircleIcon = createIcon(CheckCircleSVG);
  var RemovePauseIcon = createIcon(RemovePauseSVG);
  var ForkIcon = createIcon(ForkSVG);
  var ExclamationTriangleIcon = createIcon(ExclamationTriangleSVG);
  var InfoIcon = createIcon(InfoSVG);
  var PauseIcon = createIcon(PauseSVG);
  var PlayIcon = createIcon(PlaySVG);
  var ResetIcon = createIcon(ResetSVG);
  var TachometerIcon = createIcon(TachometerSVG);
  var TimesCircleIcon = createIcon(TimesCircleSVG);
  var TimesIcon = createIcon(TimesSVG);
  var ToggleOffIcon = createIcon(ToggleOffSVG);
  var ToggleOnIcon = createIcon(ToggleOnSVG);

  // ../../node_modules/bpmn-js-token-simulation/lib/features/toggle-mode/viewer/ToggleMode.js
  function ToggleMode(eventBus, canvas, selection) {
    this._eventBus = eventBus;
    this._canvas = canvas;
    this._active = false;
    eventBus.on("diagram.init", () => {
      this._canvasParent = this._canvas.getContainer().parentNode;
      this._init();
    });
    eventBus.on("import.parse.start", () => {
      if (this._active) {
        this.toggleMode(false);
        eventBus.once("import.done", () => {
          this.toggleMode(true);
        });
      }
    });
  }
  ToggleMode.prototype._init = function() {
    this._container = domify(`
    <div class="bts-toggle-mode">
      Token Simulation <span class="bts-toggle">${ToggleOffIcon()}</span>
    </div>
  `);
    event.bind(this._container, "click", () => this.toggleMode());
    this._canvas.getContainer().appendChild(this._container);
  };
  ToggleMode.prototype.toggleMode = function(active = !this._active) {
    if (active === this._active) {
      return;
    }
    if (active) {
      this._container.innerHTML = `Token Simulation <span class="bts-toggle">${ToggleOnIcon()}</span>`;
      classes(this._canvasParent).add("simulation");
    } else {
      this._container.innerHTML = `Token Simulation <span class="bts-toggle">${ToggleOffIcon()}</span>`;
      classes(this._canvasParent).remove("simulation");
    }
    this._eventBus.fire(TOGGLE_MODE_EVENT, {
      active
    });
    this._active = active;
  };
  ToggleMode.$inject = ["eventBus", "canvas"];

  // ../../node_modules/bpmn-js-token-simulation/lib/features/toggle-mode/viewer/index.js
  var viewer_default = {
    __init__: [
      "toggleMode"
    ],
    toggleMode: ["type", ToggleMode]
  };

  // ../../node_modules/ids/dist/index.js
  function getDefaultExportFromCjs2(x) {
    return x && x.__esModule && Object.prototype.hasOwnProperty.call(x, "default") ? x["default"] : x;
  }
  var hat$1 = { exports: {} };
  var hasRequiredHat;
  function requireHat() {
    if (hasRequiredHat) return hat$1.exports;
    hasRequiredHat = 1;
    var hat2 = hat$1.exports = function(bits, base) {
      if (!base) base = 16;
      if (bits === void 0) bits = 128;
      if (bits <= 0) return "0";
      var digits = Math.log(Math.pow(2, bits)) / Math.log(base);
      for (var i = 2; digits === Infinity; i *= 2) {
        digits = Math.log(Math.pow(2, bits / i)) / Math.log(base) * i;
      }
      var rem = digits - Math.floor(digits);
      var res = "";
      for (var i = 0; i < Math.floor(digits); i++) {
        var x = Math.floor(Math.random() * base).toString(base);
        res = x + res;
      }
      if (rem) {
        var b = Math.pow(base, rem);
        var x = Math.floor(Math.random() * b).toString(base);
        res = x + res;
      }
      var parsed = parseInt(res, base);
      if (parsed !== Infinity && parsed >= Math.pow(2, bits)) {
        return hat2(bits, base);
      } else return res;
    };
    hat2.rack = function(bits, base, expandBy) {
      var fn = function(data) {
        var iters = 0;
        do {
          if (iters++ > 10) {
            if (expandBy) bits += expandBy;
            else throw new Error("too many ID collisions, use more bits");
          }
          var id = hat2(bits, base);
        } while (Object.hasOwnProperty.call(hats, id));
        hats[id] = data;
        return id;
      };
      var hats = fn.hats = {};
      fn.get = function(id) {
        return fn.hats[id];
      };
      fn.set = function(id, value) {
        fn.hats[id] = value;
        return fn;
      };
      fn.bits = bits || 128;
      fn.base = base || 16;
      return fn;
    };
    return hat$1.exports;
  }
  var hatExports = requireHat();
  var hat = /* @__PURE__ */ getDefaultExportFromCjs2(hatExports);
  function Ids(seed) {
    if (!(this instanceof Ids)) {
      return new Ids(seed);
    }
    seed = seed || [128, 36, 1];
    this._seed = seed.length ? hat.rack(seed[0], seed[1], seed[2]) : seed;
  }
  Ids.prototype.next = function(element) {
    return this._seed(element || true);
  };
  Ids.prototype.nextPrefixed = function(prefix, element) {
    var id;
    do {
      id = prefix + this.next(true);
    } while (this.assigned(id));
    this.claim(id, element);
    return id;
  };
  Ids.prototype.claim = function(id, element) {
    this._seed.set(id, element || true);
  };
  Ids.prototype.assigned = function(id) {
    return this._seed.get(id) || false;
  };
  Ids.prototype.unclaim = function(id) {
    delete this._seed.hats[id];
  };
  Ids.prototype.clear = function() {
    var hats = this._seed.hats, id;
    for (id in hats) {
      this.unclaim(id);
    }
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/ScopeTraits.js
  var ACTIVATED = 1;
  var RUNNING = 1 << 1;
  var ENDING = 1 << 2;
  var ENDED = 1 << 3;
  var DESTROYED = 1 << 4;
  var FAILED = 1 << 5;
  var TERMINATED = 1 << 6;
  var CANCELED = 1 << 7;
  var COMPLETED = 1 << 8;
  var COMPENSABLE = 1 << 9;
  var ACTIVE = ACTIVATED | RUNNING | ENDING;
  var NOT_DEAD = ACTIVATED | ENDED;
  var ScopeTraits = Object.freeze({
    ACTIVATED,
    RUNNING,
    ENDING,
    ENDED,
    DESTROYED,
    FAILED,
    TERMINATED,
    CANCELED,
    COMPLETED,
    COMPENSABLE,
    ACTIVE,
    NOT_DEAD
  });

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/ScopeStates.js
  var SELF = {};
  function illegalTransition(state, target) {
    throw new Error(`illegal transition: ${state.name} -> ${target}`);
  }
  function orSelf(state, self) {
    if (state === SELF) {
      return self;
    }
    return state;
  }
  var ScopeState = class {
    /**
     * @param {string} name
     * @param {number} traits
     * @param {object} [transitions]
     * @param {ScopeState} [transitions.start]
     * @param {ScopeState} [transitions.cancel]
     * @param {ScopeState} [transitions.complete]
     * @param {ScopeState} [transitions.destroy]
     * @param {ScopeState} [transitions.fail]
     * @param {ScopeState} [transitions.terminate]
     * @param {ScopeState} [transitions.compensable]
     */
    constructor(name, traits, transitions = {}) {
      this.name = name;
      this.traits = traits;
      this.setTransitions(transitions);
    }
    /**
     * @param {object} transitions
     * @param {ScopeState} [transitions.start]
     * @param {ScopeState} [transitions.cancel]
     * @param {ScopeState} [transitions.complete]
     * @param {ScopeState} [transitions.destroy]
     * @param {ScopeState} [transitions.fail]
     * @param {ScopeState} [transitions.terminate]
     * @param {ScopeState} [transitions.compensable]
     */
    setTransitions({
      start,
      cancel,
      complete,
      destroy,
      fail,
      terminate,
      compensable
    }) {
      this._start = orSelf(start, this);
      this._compensable = orSelf(compensable, this);
      this._cancel = orSelf(cancel, this);
      this._complete = orSelf(complete, this);
      this._destroy = orSelf(destroy, this);
      this._fail = orSelf(fail, this);
      this._terminate = orSelf(terminate, this);
    }
    /**
     * @param {number} trait
     * @return {boolean}
     */
    hasTrait(trait) {
      return (this.traits & trait) !== 0;
    }
    /**
     * @return {ScopeState}
     */
    complete() {
      return this._complete || illegalTransition(this, "complete");
    }
    /**
     * @return {ScopeState}
     */
    destroy() {
      return this._destroy || illegalTransition(this, "destroy");
    }
    /**
     * @return {ScopeState}
     */
    cancel() {
      return this._cancel || illegalTransition(this, "cancel");
    }
    /**
     * @return {ScopeState}
     */
    fail() {
      return this._fail || illegalTransition(this, "fail");
    }
    /**
     * @return {ScopeState}
     */
    terminate() {
      return this._terminate || illegalTransition(this, "terminate");
    }
    /**
     * @return {ScopeState}
     */
    compensable() {
      return this._compensable || illegalTransition(this, "compensable");
    }
    /**
     * @return {ScopeState}
     */
    start() {
      return this._start || illegalTransition(this, "start");
    }
  };
  var FAILED2 = new ScopeState("failed", ScopeTraits.DESTROYED | ScopeTraits.FAILED);
  var TERMINATED2 = new ScopeState("terminated", ScopeTraits.DESTROYED | ScopeTraits.TERMINATED | ScopeTraits.COMPLETED);
  var COMPLETED2 = new ScopeState("completed", ScopeTraits.DESTROYED | ScopeTraits.COMPLETED);
  var TERMINATING = new ScopeState("terminating", ScopeTraits.ENDING | ScopeTraits.TERMINATED | ScopeTraits.COMPLETED, {
    destroy: TERMINATED2
  });
  var CANCELING = new ScopeState("canceling", ScopeTraits.ENDING | ScopeTraits.FAILED | ScopeTraits.CANCELED, {
    destroy: FAILED2,
    complete: SELF,
    terminate: TERMINATING
  });
  var COMPLETING = new ScopeState("completing", ScopeTraits.ENDING | ScopeTraits.COMPLETED, {
    destroy: COMPLETED2,
    cancel: CANCELING,
    terminate: TERMINATING
  });
  var FAILING = new ScopeState("failing", ScopeTraits.ENDING | ScopeTraits.FAILED, {
    cancel: CANCELING,
    complete: COMPLETING,
    destroy: FAILED2,
    terminate: TERMINATING
  });
  var COMPENSABLE_COMPLETED = new ScopeState("compensable:completed", ScopeTraits.ENDED | ScopeTraits.COMPLETED);
  var COMPENSABLE_COMPLETING = new ScopeState("compensable:completing", ScopeTraits.ENDING | ScopeTraits.COMPLETED, {
    destroy: COMPENSABLE_COMPLETED,
    terminate: TERMINATING,
    compensable: SELF
  });
  var COMPENSABLE_FAILING = new ScopeState("compensable:failing", ScopeTraits.ENDING | ScopeTraits.FAILED, {
    complete: COMPENSABLE_COMPLETING,
    terminate: TERMINATING,
    destroy: FAILED2
  });
  COMPENSABLE_COMPLETED.setTransitions({
    cancel: CANCELING,
    fail: COMPENSABLE_FAILING,
    destroy: COMPLETED2,
    compensable: SELF
  });
  var COMPENSABLE_RUNNING = new ScopeState("compensable:running", ScopeTraits.RUNNING | ScopeTraits.COMPENSABLE, {
    cancel: CANCELING,
    complete: COMPENSABLE_COMPLETING,
    compensable: SELF,
    destroy: COMPENSABLE_COMPLETED,
    fail: COMPENSABLE_FAILING,
    terminate: TERMINATING
  });
  var RUNNING2 = new ScopeState("running", ScopeTraits.RUNNING, {
    cancel: CANCELING,
    complete: COMPLETING,
    compensable: COMPENSABLE_RUNNING,
    destroy: TERMINATED2,
    fail: FAILING,
    terminate: TERMINATING
  });
  var ACTIVATED2 = new ScopeState("activated", ScopeTraits.ACTIVATED, {
    start: RUNNING2,
    destroy: TERMINATED2
  });
  var ScopeStates = Object.freeze({
    ACTIVATED: ACTIVATED2,
    RUNNING: RUNNING2,
    CANCELING,
    COMPLETING,
    COMPLETED: COMPLETED2,
    FAILING,
    FAILED: FAILED2,
    TERMINATING,
    TERMINATED: TERMINATED2
  });

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/Scope.js
  var Scope = class {
    /**
     * @param {string} id
     * @param {Element} element
     * @param {Scope} parent
     * @param {Scope} initiator
     *
     * @constructor
     */
    constructor(id, element, parent = null, initiator = null) {
      this.id = id;
      this.element = element;
      this.parent = parent;
      this.initiator = initiator;
      this.subscriptions = /* @__PURE__ */ new Set();
      this.children = [];
      this.state = ScopeStates.ACTIVATED;
    }
    /**
     * @return {boolean}
     */
    get running() {
      return this.hasTrait(ScopeTraits.RUNNING);
    }
    /**
     * @return {boolean}
     */
    get destroyed() {
      return this.hasTrait(ScopeTraits.DESTROYED);
    }
    /**
     * @return {boolean}
     */
    get completed() {
      return this.hasTrait(ScopeTraits.COMPLETED);
    }
    /**
     * @return {boolean}
     */
    get canceled() {
      return this.hasTrait(ScopeTraits.CANCELED);
    }
    /**
     * @return {boolean}
     */
    get failed() {
      return this.hasTrait(ScopeTraits.FAILED);
    }
    get active() {
      return this.hasTrait(ScopeTraits.ACTIVE);
    }
    /**
     * @param {number} phase
     * @return {boolean}
     */
    hasTrait(trait) {
      return this.state.hasTrait(trait);
    }
    /**
     * Start the scope
     *
     * @return {Scope}
     */
    start() {
      this.state = this.state.start();
      return this;
    }
    /**
     * Make this scope compensable.
     *
     * @return {Scope}
     */
    compensable() {
      this.state = this.state.compensable();
      return this;
    }
    /**
     * @param {Scope} initiator
     *
     * @return {Scope}
     */
    fail(initiator) {
      if (!this.failed) {
        this.state = this.state.fail();
        this.failInitiator = initiator;
      }
      return this;
    }
    cancel(initiator) {
      if (!this.canceled) {
        this.state = this.state.cancel();
        this.cancelInitiator = initiator;
      }
      return this;
    }
    /**
     * @param {Scope} initiator
     *
     * @return {Scope}
     */
    terminate(initiator) {
      this.state = this.state.terminate();
      this.terminateInitiator = initiator;
      return this;
    }
    /**
     * @return {Scope}
     */
    complete() {
      this.state = this.state.complete();
      return this;
    }
    /**
     * Destroy the scope
     *
     * @param {Scope} initiator
     *
     * @return {Scope}
     */
    destroy(initiator) {
      this.state = this.state.destroy();
      this.destroyInitiator = initiator;
      return this;
    }
    /**
     * @return {number}
     */
    getTokens() {
      return this.children.filter((c) => !c.destroyed).length;
    }
    /**
     * @param {Element} element
     *
     * @return {number}
     */
    getTokensByElement(element) {
      return this.children.filter((c) => !c.destroyed && c.element === element).length;
    }
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/util/SetUtil.js
  function filterSet(set, matchFn) {
    const matched = [];
    for (const el of set) {
      if (matchFn(el)) {
        matched.push(el);
      }
    }
    return matched;
  }
  function findSet(set, matchFn) {
    for (const el of set) {
      if (matchFn(el)) {
        return el;
      }
    }
    return null;
  }

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/util/EventsUtil.js
  function eventsMatch(a, b) {
    const attrMatch = ["type", "name", "iref"].every((attr2) => !(attr2 in a) || a[attr2] === b[attr2]);
    const catchAllMatch = !b.ref && (b.type === "error" || b.type === "escalation");
    return attrMatch && (catchAllMatch || refsMatch(a, b));
  }
  function refsMatch(a, b) {
    const attr2 = "ref";
    return !(attr2 in a) || a[attr2] === b[attr2];
  }

  // ../../node_modules/bpmn-js/lib/util/ModelUtil.js
  function is(element, type) {
    var bo = getBusinessObject(element);
    return bo && typeof bo.$instanceOf === "function" && bo.$instanceOf(type);
  }
  function isAny(element, types) {
    return some(types, function(t) {
      return is(element, t);
    });
  }
  function getBusinessObject(element) {
    return element && element.businessObject || element;
  }
  function getDi(element) {
    return element && element.di;
  }

  // ../../node_modules/bpmn-js/lib/util/DrilldownUtil.js
  var planeSuffix = "_plane";
  function getPlaneIdFromShape(element) {
    var id = element.id;
    if (is(element, "bpmn:SubProcess")) {
      return addPlaneSuffix(id);
    }
    return id;
  }
  function isPlane(element) {
    var di = getDi(element);
    return is(di, "bpmndi:BPMNPlane");
  }
  function addPlaneSuffix(id) {
    return id + planeSuffix;
  }

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/util/ModelUtil.js
  function filterSequenceFlows(flows) {
    return flows.filter((f) => is(f, "bpmn:SequenceFlow"));
  }
  function isMessageFlow(element) {
    return is(element, "bpmn:MessageFlow");
  }
  function isSequenceFlow(element) {
    return is(element, "bpmn:SequenceFlow");
  }
  function isLinkCatch(element) {
    return isCatchEvent(element) && isTypedEvent(element, "bpmn:LinkEventDefinition");
  }
  function isLinkThrow(element) {
    return is(element, "bpmn:IntermediateThrowEvent") && isTypedEvent(element, "bpmn:LinkEventDefinition");
  }
  function isCompensationEvent(element) {
    return isCatchEvent(element) && isTypedEvent(element, "bpmn:CompensateEventDefinition");
  }
  function isCompensationActivity(element) {
    return is(element, "bpmn:Activity") && element.businessObject.isForCompensation;
  }
  function isCatchEvent(element) {
    return (is(element, "bpmn:CatchEvent") || is(element, "bpmn:ReceiveTask")) && !isLabel(element);
  }
  function isBoundaryEvent(element) {
    return is(element, "bpmn:BoundaryEvent") && !isLabel(element);
  }
  function isNoneStartEvent(element) {
    return isStartEvent(element) && !isTypedEvent(element);
  }
  function isImplicitStartEvent(element) {
    if (isLabel(element)) {
      return false;
    }
    if (!isAny2(element, [
      "bpmn:Activity",
      "bpmn:IntermediateCatchEvent",
      "bpmn:IntermediateThrowEvent",
      "bpmn:Gateway",
      "bpmn:EndEvent"
    ])) {
      return false;
    }
    if (isLinkCatch(element)) {
      return false;
    }
    const incoming = element.incoming.find(isSequenceFlow);
    if (incoming) {
      return false;
    }
    if (isCompensationActivity(element)) {
      return false;
    }
    if (isEventSubProcess(element)) {
      return false;
    }
    return true;
  }
  function isStartEvent(element) {
    return is(element, "bpmn:StartEvent") && !isLabel(element);
  }
  function isLabel(element) {
    return !!element.labelTarget;
  }
  function isEventSubProcess(element) {
    return getBusinessObject(element).triggeredByEvent;
  }
  function isInterrupting(element) {
    return is(element, "bpmn:StartEvent") && getBusinessObject(element).isInterrupting || is(element, "bpmn:BoundaryEvent") && getBusinessObject(element).cancelActivity;
  }
  function isAny2(element, types) {
    return types.some((type) => is(element, type));
  }
  function isTypedEvent(event2, eventDefinitionType) {
    return some(getBusinessObject(event2).eventDefinitions, (definition) => {
      return eventDefinitionType ? is(definition, eventDefinitionType) : true;
    });
  }
  function getChildren(element, elementRegistry) {
    if (element.children && element.children.length !== 0) {
      return element.children;
    }
    if (is(element, "bpmn:SubProcess") && !element.di.isExpanded) {
      return elementRegistry.get(getPlaneIdFromShape(element)).children;
    }
    return [];
  }

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/Simulator.js
  function Simulator(injector, eventBus, elementRegistry) {
    const ids = injector.get("scopeIds", false) || new Ids([32, 36]);
    const configuration = {};
    const behaviors = {};
    const noopBehavior = new NoopBehavior();
    const changedElements = /* @__PURE__ */ new Set();
    const jobs = [];
    const scopes = /* @__PURE__ */ new Set();
    const subscriptions = /* @__PURE__ */ new Set();
    on("tick", function() {
      for (const element of changedElements) {
        emit("elementChanged", {
          element
        });
      }
      changedElements.clear();
    });
    function queue(scope, task) {
      jobs.push([task, scope]);
      if (jobs.length !== 1) {
        return;
      }
      let next;
      while (next = jobs[0]) {
        const [task2, scope2] = next;
        if (!scope2.destroyed) {
          task2();
        }
        jobs.shift();
      }
      emit("tick");
    }
    function getBehavior(element) {
      return behaviors[element.type] || noopBehavior;
    }
    function signal(context) {
      const {
        element,
        parentScope,
        initiator = null,
        scope = initializeScope({
          element,
          parent: parentScope,
          initiator
        })
      } = context;
      queue(scope, function() {
        if (!scope.running) {
          scope.start();
        }
        trace("signal", {
          ...context,
          scope
        });
        getBehavior(element).signal({
          ...context,
          scope
        });
        if (scope.parent) {
          scopeChanged(scope.parent);
        }
      });
      return scope;
    }
    function enter(context) {
      const {
        element,
        scope: parentScope,
        initiator = parentScope
      } = context;
      const scope = initializeScope({
        element,
        parent: parentScope,
        initiator
      });
      queue(scope, function() {
        if (!scope.running) {
          scope.start();
        }
        trace("enter", context);
        getBehavior(element).enter({
          ...context,
          initiator,
          scope
        });
        if (scope.parent) {
          scopeChanged(scope.parent);
        }
      });
      return scope;
    }
    function exit(context) {
      const {
        element,
        scope,
        initiator = scope
      } = context;
      queue(scope, function() {
        trace("exit", context);
        getBehavior(element).exit({
          ...context,
          initiator
        });
        if (scope.running) {
          scope.complete();
        }
        destroyScope(scope, initiator);
        scope.parent && scopeChanged(scope.parent);
      });
    }
    function trigger(context) {
      const {
        event: _event,
        initiator,
        scope
      } = context;
      const event2 = getEvent(_event);
      const subscriptions2 = scope.subscriptions;
      let matchingSubscriptions = filterSet(
        subscriptions2,
        (subscription) => eventsMatch(event2, subscription.event)
      );
      if (event2.type === "error" || event2.type === "escalation") {
        const referenceSubscriptions = filterSet(
          matchingSubscriptions,
          (subscription) => refsMatch(event2, subscription.event)
        );
        if (matchingSubscriptions.every((subscription) => subscription.event.boundary) && referenceSubscriptions.some((subscription) => subscription.event.boundary) || referenceSubscriptions.some((subscription) => !subscription.event.boundary)) {
          matchingSubscriptions = referenceSubscriptions;
        }
      }
      const nonInterrupting = matchingSubscriptions.filter(
        (subscription) => !subscription.event.interrupting
      );
      const interrupting = matchingSubscriptions.filter(
        (subscription) => subscription.event.interrupting
      );
      if (!interrupting.length) {
        return nonInterrupting.map(
          (subscription) => subscription.triggerFn(initiator)
        ).flat();
      }
      const interrupt = interrupting.find((subscription) => !subscription.event.boundary) || interrupting[0];
      const remainingSubscriptions = filterSet(
        subscriptions2,
        (subscription) => subscription.event.persistent || isRethrow(subscription.event, interrupt.event)
      );
      subscriptions2.forEach((subscription) => {
        if (!remainingSubscriptions.includes(subscription)) {
          subscription.remove();
        }
      });
      return [interrupt.triggerFn(initiator)].flat().filter((s) => s);
    }
    function subscribe(scope, event2, triggerFn) {
      event2 = getEvent(event2);
      const element = event2.element;
      const subscription = {
        scope,
        event: event2,
        element,
        triggerFn,
        remove() {
          unsubscribe(subscription);
        }
      };
      subscriptions.add(subscription);
      scope.subscriptions.add(subscription);
      if (element) {
        elementChanged(element);
      }
      return subscription;
    }
    function unsubscribe(subscription) {
      const {
        scope,
        event: event2
      } = subscription;
      subscriptions.delete(subscription);
      scope.subscriptions.delete(subscription);
      if (event2.element) {
        elementChanged(event2.element);
      }
    }
    function createInternalRef(element) {
      if (is(element, "bpmn:StartEvent") || is(element, "bpmn:IntermediateCatchEvent") || is(element, "bpmn:ReceiveTask") || isSpecialBoundaryEvent(element)) {
        return getBusinessObject(element).name || element.id;
      }
      return null;
    }
    function getNoneEvent(element) {
      return {
        element,
        interrupting: false,
        boundary: false,
        iref: element.id,
        type: "none"
      };
    }
    function getEvent(element) {
      if (!element.businessObject) {
        return element;
      }
      const interrupting = isInterrupting(element);
      const boundary = isBoundaryEvent(element);
      const iref = createInternalRef(element);
      const baseEvent = {
        element,
        interrupting,
        boundary,
        ...iref ? { iref } : {}
      };
      const eventDefinition = getEventDefinitions(element)[0];
      if (!eventDefinition) {
        return {
          ...baseEvent,
          type: isImplicitMessageCatch(element) ? "message" : "none"
        };
      }
      if (is(eventDefinition, "bpmn:LinkEventDefinition")) {
        return {
          ...baseEvent,
          type: "link",
          name: eventDefinition.name
        };
      }
      if (is(eventDefinition, "bpmn:SignalEventDefinition")) {
        return {
          ...baseEvent,
          type: "signal",
          ref: eventDefinition.signalRef
        };
      }
      if (is(eventDefinition, "bpmn:TimerEventDefinition")) {
        return {
          ...baseEvent,
          type: "timer"
        };
      }
      if (is(eventDefinition, "bpmn:ConditionalEventDefinition")) {
        return {
          ...baseEvent,
          type: "condition"
        };
      }
      if (is(eventDefinition, "bpmn:EscalationEventDefinition")) {
        return {
          ...baseEvent,
          type: "escalation",
          ref: eventDefinition.escalationRef
        };
      }
      if (is(eventDefinition, "bpmn:CancelEventDefinition")) {
        return {
          ...baseEvent,
          type: "cancel"
        };
      }
      if (is(eventDefinition, "bpmn:ErrorEventDefinition")) {
        return {
          ...baseEvent,
          type: "error",
          ref: eventDefinition.errorRef
        };
      }
      if (is(eventDefinition, "bpmn:MessageEventDefinition")) {
        return {
          ...baseEvent,
          type: "message",
          ref: eventDefinition.messageRef
        };
      }
      if (is(eventDefinition, "bpmn:CompensateEventDefinition")) {
        let ref = eventDefinition.activityRef && elementRegistry.get(eventDefinition.activityRef.id);
        if (!ref) {
          if (isStartEvent(element) && isEventSubProcess(element.parent)) {
            ref = element.parent.parent;
          } else if (isBoundaryEvent(element)) {
            ref = element.host;
          } else {
            ref = element.parent;
          }
        }
        return {
          ...baseEvent,
          type: "compensate",
          ref,
          persistent: true
        };
      }
      throw new Error("unknown event definition", eventDefinition);
    }
    function createScope(context, emitEvent = true) {
      const {
        element,
        parent: parentScope,
        initiator
      } = context;
      emitEvent && trace("createScope", {
        element,
        scope: parentScope
      });
      const scope = new Scope(ids.next(), element, parentScope, initiator);
      if (parentScope) {
        parentScope.children.push(scope);
      }
      scopes.add(scope);
      emitEvent && emit("createScope", {
        scope
      });
      elementChanged(element);
      if (parentScope) {
        elementChanged(parentScope.element);
      }
      return scope;
    }
    function subscriptionFilter(filter) {
      if (typeof filter === "function") {
        return filter;
      }
      const {
        event: _event,
        element,
        scope
      } = filter;
      const elements = filter.elements || element && [element];
      const event2 = _event && getEvent(_event);
      return ((subscription) => (!event2 || eventsMatch(event2, subscription.event)) && (!elements || elements.includes(subscription.element)) && (!scope || scope === subscription.scope));
    }
    function scopeSubscriptionFilter(event2) {
      const matchesSubscription = event2 === "function" ? event2 : subscriptionFilter(event2);
      return ((scope) => Array.from(scope.subscriptions).some(matchesSubscription));
    }
    function scopeFilter(filter) {
      if (typeof filter === "function") {
        return filter;
      }
      const {
        element,
        waitsOnElement,
        parent,
        trait = ScopeTraits.RUNNING,
        subscribedTo
      } = filter;
      const isSubscribed = subscribedTo ? scopeSubscriptionFilter(subscribedTo) : () => true;
      return ((scope) => (!element || scope.element === element) && (!parent || scope.parent === parent) && (!waitsOnElement || scope.getTokensByElement(waitsOnElement) > 0) && scope.hasTrait(trait) && isSubscribed(scope));
    }
    function findSubscriptions(filter) {
      return filterSet(subscriptions, subscriptionFilter(filter));
    }
    function findSubscription(filter) {
      return findSet(subscriptions, subscriptionFilter(filter));
    }
    function findScopes(filter) {
      return filterSet(scopes, scopeFilter(filter));
    }
    function findScope(filter) {
      return findSet(scopes, scopeFilter(filter));
    }
    function destroyScope(scope, initiator = null) {
      if (scope.destroyed) {
        return;
      }
      scope.destroy(initiator);
      for (const subscription of scope.subscriptions) {
        const trait = subscription.event.traits || ScopeTraits.ACTIVE;
        if (!scope.hasTrait(trait)) {
          unsubscribe(subscription);
        }
      }
      if (scope.destroyed) {
        for (const childScope of scope.children) {
          if (!childScope.destroyed) {
            destroyScope(childScope, initiator);
          }
        }
        trace("destroyScope", {
          element: scope.element,
          scope
        });
        scopes.delete(scope);
        emit("destroyScope", {
          scope
        });
      }
      elementChanged(scope.element);
      if (scope.parent) {
        elementChanged(scope.parent.element);
      }
    }
    function trace(action, context) {
      emit("trace", {
        ...context,
        action
      });
    }
    function elementChanged(element) {
      changedElements.add(element);
      if (!jobs.length) {
        emit("tick");
      }
    }
    function scopeChanged(scope) {
      emit("scopeChanged", {
        scope
      });
    }
    function emit(event2, payload = {}) {
      return eventBus.fire(`tokenSimulation.simulator.${event2}`, payload);
    }
    function on(event2, callback) {
      eventBus.on("tokenSimulation.simulator." + event2, callback);
    }
    function off(event2, callback) {
      eventBus.off("tokenSimulation.simulator." + event2, callback);
    }
    function setConfig(element, updatedConfig) {
      const existingConfig = getConfig(element);
      configuration[element.id || element] = {
        ...existingConfig,
        ...updatedConfig
      };
      elementChanged(element);
    }
    function initializeRootScopes() {
      const rootScopes = [];
      elementRegistry.forEach((element) => {
        if (!isAny2(element, ["bpmn:Process", "bpmn:Participant"])) {
          return;
        }
        const scope = createScope({
          element
        }, false);
        rootScopes.push(scope);
        const startEvents = element.children.filter(isStartEvent);
        const implicitStartEvents = element.children.filter(isImplicitStartEvent);
        for (const startEvent of startEvents) {
          const event2 = {
            ...getEvent(startEvent),
            interrupting: false
          };
          subscribe(scope, event2, (initiator) => signal({
            element,
            startEvent,
            initiator
          }));
        }
        if (!startEvents.length) {
          for (const implicitStartEvent of implicitStartEvents) {
            const event2 = getNoneEvent(implicitStartEvent);
            subscribe(scope, event2, (initiator) => signal({
              element,
              initiator
            }));
          }
        }
      });
      return rootScopes;
    }
    function initializeScope(context) {
      const {
        element
      } = context;
      const scope = createScope(context);
      const {
        attachers = []
      } = element;
      const children = getChildren(element, elementRegistry);
      for (const childElement of children) {
        if (isEventSubProcess(childElement)) {
          const startEvents = getChildren(childElement, elementRegistry).filter(
            (element2) => isStartEvent(element2) && !isCompensationEvent(element2)
          );
          for (const startEvent of startEvents) {
            subscribe(scope, startEvent, (initiator) => {
              return signal({
                element: childElement,
                parentScope: scope,
                startEvent,
                initiator
              });
            });
          }
        }
      }
      for (const attacher of attachers) {
        if (isBoundaryEvent(attacher) && !isCompensationEvent(attacher)) {
          subscribe(scope, attacher, (initiator) => {
            return signal({
              element: attacher,
              parentScope: scope.parent,
              hostScope: scope,
              initiator
            });
          });
        }
      }
      return scope;
    }
    function getConfig(element) {
      return configuration[element.id || element] || {};
    }
    function waitForScopes(scope, scopes2) {
      if (!scopes2.length) {
        return;
      }
      const event2 = {
        type: "all-completed",
        persistent: false
      };
      const remainingScopes = new Set(scopes2);
      const destroyListener = (destroyEvent) => {
        remainingScopes.delete(destroyEvent.scope);
        if (remainingScopes.size === 0) {
          off("destroyScope", destroyListener);
          trigger({
            scope,
            event: event2
          });
        }
      };
      on("destroyScope", destroyListener);
      return event2;
    }
    function waitAtElement(element, wait = true) {
      setConfig(element, {
        wait
      });
    }
    function reset() {
      for (const scope of scopes) {
        destroyScope(scope);
      }
      for (const rootScope of initializeRootScopes()) {
        scopes.add(rootScope);
      }
      emit("tick");
      emit("reset");
    }
    this.createScope = createScope;
    this.destroyScope = destroyScope;
    this.findScope = findScope;
    this.findScopes = findScopes;
    this.findSubscription = findSubscription;
    this.findSubscriptions = findSubscriptions;
    this.waitAtElement = waitAtElement;
    this.waitForScopes = waitForScopes;
    this.setConfig = setConfig;
    this.getConfig = getConfig;
    this.signal = signal;
    this.enter = enter;
    this.exit = exit;
    this.subscribe = subscribe;
    this.trigger = trigger;
    this.reset = reset;
    this.on = on;
    this.off = off;
    this.registerBehavior = function(element, behavior) {
      behaviors[element] = behavior;
    };
  }
  Simulator.$inject = [
    "injector",
    "eventBus",
    "elementRegistry"
  ];
  function NoopBehavior() {
    this.signal = function(context) {
      console.log("ignored #exit", context.element);
    };
    this.exit = function(context) {
      console.log("ignored #exit", context.element);
    };
    this.enter = function(context) {
      console.log("ignored #enter", context.element);
    };
  }
  function isRethrow(event2, interrupt) {
    return event2.boundary && !interrupt.boundary;
  }
  function isImplicitMessageCatch(element) {
    return is(element, "bpmn:ReceiveTask") || element.incoming.some((element2) => is(element2, "bpmn:MessageFlow"));
  }
  function isSpecialBoundaryEvent(element) {
    if (!isBoundaryEvent(element)) {
      return false;
    }
    const eventDefinitions = getEventDefinitions(element);
    return !eventDefinitions[0] || isAny2(eventDefinitions[0], [
      "bpmn:ConditionalEventDefinition",
      "bpmn:TimerEventDefinition"
    ]);
  }
  function getEventDefinitions(element) {
    return element.businessObject.get("eventDefinitions") || [];
  }

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/behaviors/StartEventBehavior.js
  function StartEventBehavior(simulator, activityBehavior) {
    this._simulator = simulator;
    this._activityBehavior = activityBehavior;
    simulator.registerBehavior("bpmn:StartEvent", this);
  }
  StartEventBehavior.prototype.signal = function(context) {
    this._simulator.exit(context);
  };
  StartEventBehavior.prototype.exit = function(context) {
    this._activityBehavior.exit(context);
  };
  StartEventBehavior.$inject = [
    "simulator",
    "activityBehavior"
  ];

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/behaviors/EndEventBehavior.js
  function EndEventBehavior(simulator, scopeBehavior, intermediateThrowEventBehavior) {
    this._intermediateThrowEventBehavior = intermediateThrowEventBehavior;
    this._scopeBehavior = scopeBehavior;
    simulator.registerBehavior("bpmn:EndEvent", this);
  }
  EndEventBehavior.$inject = [
    "simulator",
    "scopeBehavior",
    "intermediateThrowEventBehavior"
  ];
  EndEventBehavior.prototype.enter = function(context) {
    this._intermediateThrowEventBehavior.enter(context);
  };
  EndEventBehavior.prototype.signal = function(context) {
    this._intermediateThrowEventBehavior.signal(context);
  };
  EndEventBehavior.prototype.exit = function(context) {
    const {
      scope
    } = context;
    this._scopeBehavior.tryExit(scope.parent, scope);
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/behaviors/BoundaryEventBehavior.js
  function BoundaryEventBehavior(simulator, activityBehavior, scopeBehavior) {
    this._simulator = simulator;
    this._activityBehavior = activityBehavior;
    this._scopeBehavior = scopeBehavior;
    simulator.registerBehavior("bpmn:BoundaryEvent", this);
  }
  BoundaryEventBehavior.prototype.signal = function(context) {
    const {
      element,
      scope,
      hostScope = this._simulator.findScope({
        parent: scope.parent,
        element: element.host
      })
    } = context;
    if (!hostScope) {
      throw new Error("host scope not found");
    }
    const cancelActivity = getBusinessObject(element).cancelActivity;
    if (cancelActivity) {
      this._scopeBehavior.interrupt(hostScope, scope);
      const event2 = this._scopeBehavior.tryExit(hostScope, scope);
      if (event2) {
        const subscription = this._simulator.subscribe(hostScope, event2, (initiator) => {
          subscription.remove();
          return this._simulator.exit(context);
        });
        return;
      }
    }
    this._simulator.exit(context);
  };
  BoundaryEventBehavior.prototype.exit = function(context) {
    this._activityBehavior.exit(context);
  };
  BoundaryEventBehavior.$inject = [
    "simulator",
    "activityBehavior",
    "scopeBehavior"
  ];

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/behaviors/IntermediateCatchEventBehavior.js
  function IntermediateCatchEventBehavior(simulator, activityBehavior) {
    this._activityBehavior = activityBehavior;
    this._simulator = simulator;
    simulator.registerBehavior("bpmn:IntermediateCatchEvent", this);
    simulator.registerBehavior("bpmn:ReceiveTask", this);
  }
  IntermediateCatchEventBehavior.$inject = [
    "simulator",
    "activityBehavior"
  ];
  IntermediateCatchEventBehavior.prototype.signal = function(context) {
    return this._simulator.exit(context);
  };
  IntermediateCatchEventBehavior.prototype.enter = function(context) {
    const {
      element
    } = context;
    return this._activityBehavior.signalOnEvent(context, element);
  };
  IntermediateCatchEventBehavior.prototype.exit = function(context) {
    this._activityBehavior.exit(context);
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/behaviors/IntermediateThrowEventBehavior.js
  function IntermediateThrowEventBehavior(simulator, activityBehavior, eventBehaviors) {
    this._simulator = simulator;
    this._activityBehavior = activityBehavior;
    this._eventBehaviors = eventBehaviors;
    simulator.registerBehavior("bpmn:IntermediateThrowEvent", this);
    simulator.registerBehavior("bpmn:SendTask", this);
  }
  IntermediateThrowEventBehavior.prototype.enter = function(context) {
    const {
      element
    } = context;
    const eventBehavior = this._eventBehaviors.get(element);
    if (eventBehavior) {
      const event2 = eventBehavior(context);
      if (event2) {
        return this._activityBehavior.signalOnEvent(context, event2);
      }
    }
    this._activityBehavior.enter(context);
  };
  IntermediateThrowEventBehavior.prototype.signal = function(context) {
    this._activityBehavior.signal(context);
  };
  IntermediateThrowEventBehavior.prototype.exit = function(context) {
    this._activityBehavior.exit(context);
  };
  IntermediateThrowEventBehavior.$inject = [
    "simulator",
    "activityBehavior",
    "eventBehaviors"
  ];

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/behaviors/ExclusiveGatewayBehavior.js
  function ExclusiveGatewayBehavior(simulator, scopeBehavior) {
    this._scopeBehavior = scopeBehavior;
    this._simulator = simulator;
    simulator.registerBehavior("bpmn:ExclusiveGateway", this);
  }
  ExclusiveGatewayBehavior.prototype.enter = function(context) {
    this._simulator.exit(context);
  };
  ExclusiveGatewayBehavior.prototype.exit = function(context) {
    const {
      element,
      scope
    } = context;
    const outgoings = filterSequenceFlows(element.outgoing);
    if (outgoings.length === 1) {
      return this._simulator.enter({
        element: outgoings[0],
        scope: scope.parent
      });
    }
    const {
      activeOutgoing
    } = this._simulator.getConfig(element);
    const outgoing = outgoings.find((o) => o === activeOutgoing);
    if (!outgoing) {
      return this._scopeBehavior.tryExit(scope.parent, scope);
    }
    return this._simulator.enter({
      element: outgoing,
      scope: scope.parent
    });
  };
  ExclusiveGatewayBehavior.$inject = [
    "simulator",
    "scopeBehavior"
  ];

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/behaviors/ParallelGatewayBehavior.js
  function ParallelGatewayBehavior(simulator, activityBehavior) {
    this._simulator = simulator;
    this._activityBehavior = activityBehavior;
    simulator.registerBehavior("bpmn:ParallelGateway", this);
  }
  ParallelGatewayBehavior.prototype.enter = function(context) {
    const {
      scope
    } = context;
    const joiningScopes = this._findJoiningScopes(context);
    if (joiningScopes.length) {
      for (const childScope of joiningScopes) {
        if (childScope !== scope) {
          this._simulator.destroyScope(childScope.complete(), scope);
        }
      }
      this._simulator.exit(context);
    }
  };
  ParallelGatewayBehavior.prototype._findJoiningScopes = function(enterContext) {
    const {
      scope,
      element
    } = enterContext;
    const sequenceFlows = filterSequenceFlows(element.incoming);
    const {
      parent: parentScope
    } = scope;
    const elementScopes = this._simulator.findScopes({
      parent: parentScope,
      element
    });
    const matchingScopes = sequenceFlows.map(
      (flow) => elementScopes.find((scope2) => scope2.initiator.element === flow)
    ).filter((scope2) => scope2);
    if (matchingScopes.length === sequenceFlows.length) {
      return matchingScopes;
    } else {
      return [];
    }
  };
  ParallelGatewayBehavior.prototype.exit = function(context) {
    this._activityBehavior.exit(context);
  };
  ParallelGatewayBehavior.$inject = [
    "simulator",
    "activityBehavior"
  ];

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/behaviors/EventBasedGatewayBehavior.js
  function EventBasedGatewayBehavior(simulator) {
    this._simulator = simulator;
    simulator.registerBehavior("bpmn:EventBasedGateway", this);
  }
  EventBasedGatewayBehavior.$inject = [
    "simulator"
  ];
  EventBasedGatewayBehavior.prototype.enter = function(context) {
    const {
      element,
      scope
    } = context;
    const parentScope = scope.parent;
    const triggerElements = getTriggers(element);
    const subscriptions = triggerElements.map(
      (triggerElement) => this._simulator.subscribe(parentScope, triggerElement, (initiator) => {
        subscriptions.forEach((subscription) => subscription.remove());
        this._simulator.destroyScope(scope, initiator);
        return this._simulator.signal({
          element: triggerElement,
          parentScope,
          initiator
        });
      })
    );
  };
  function getTriggers(element) {
    return element.outgoing.map(
      (outgoing) => outgoing.target
    ).filter((activity) => isAny2(activity, [
      "bpmn:IntermediateCatchEvent",
      "bpmn:ReceiveTask"
    ]));
  }

  // ../../node_modules/bpmn-js-token-simulation/lib/util/ElementHelper.js
  function getEventDefinition(event2, eventDefinitionType) {
    return find(getBusinessObject(event2).eventDefinitions, (definition) => {
      return is(definition, eventDefinitionType);
    });
  }
  function isTypedEvent2(event2, eventDefinitionType) {
    return some(getBusinessObject(event2).eventDefinitions, (definition) => {
      return is(definition, eventDefinitionType);
    });
  }

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/behaviors/InclusiveGatewayBehavior.js
  function InclusiveGatewayBehavior(simulator, activityBehavior) {
    this._simulator = simulator;
    this._activityBehavior = activityBehavior;
    simulator.registerBehavior("bpmn:InclusiveGateway", this);
  }
  InclusiveGatewayBehavior.prototype.enter = function(context) {
    this._tryJoin(context);
  };
  InclusiveGatewayBehavior.prototype.exit = function(context) {
    const {
      element,
      scope
    } = context;
    const outgoings = filterSequenceFlows(element.outgoing);
    if (outgoings.length > 1) {
      const {
        activeOutgoing = []
      } = this._simulator.getConfig(element);
      if (!activeOutgoing.length) {
        throw new Error("no outgoing configured");
      }
      for (const outgoing of activeOutgoing) {
        this._simulator.enter({
          element: outgoing,
          scope: scope.parent
        });
      }
    } else {
      this._activityBehavior.exit(context);
    }
  };
  InclusiveGatewayBehavior.prototype._tryJoin = function(context) {
    var exclude = context.exclude || [];
    const {
      scope,
      element
    } = context;
    const {
      parent: parentScope
    } = scope;
    const incomingSequenceFlows = filterSequenceFlows(element.incoming);
    const gatewayScopes = this._simulator.findScopes({
      parent: parentScope,
      element
    }).filter((s) => !exclude.includes(s));
    const incomingFlowsWithoutToken = incomingSequenceFlows.filter(
      (flow) => !gatewayScopes.find((s) => s.initiator.element === flow)
    );
    const incomingFlowsWithToken = incomingSequenceFlows.filter(
      (flow) => gatewayScopes.find((s) => s.initiator.element === flow)
    );
    const remainingScopes = this._getRemainingScopes(context);
    const incomingScopes = remainingScopes.filter(
      (scope2) => incomingFlowsWithoutToken.some(
        (flow) => this._canReachElement(context, scope2.element, flow)
      )
    );
    const requiredScopes = incomingScopes.filter(
      (scope2) => !incomingFlowsWithToken.some(
        (flow) => this._canReachElement(context, scope2.element, flow)
      )
    );
    if (!requiredScopes.length) {
      this._join(context, incomingFlowsWithToken, gatewayScopes, exclude);
    }
    const remainingReceivedScopes = this._simulator.findScopes({
      parent: parentScope,
      element
    }).filter((s) => !exclude.includes(s));
    if (remainingReceivedScopes[0] !== scope) {
      return;
    }
    const event2 = this._simulator.waitForScopes(scope, requiredScopes);
    const subscription = this._simulator.subscribe(scope, event2, () => {
      subscription.remove();
      this._tryJoin(context);
    });
  };
  InclusiveGatewayBehavior.prototype._getRemainingScopes = function(context) {
    const {
      scope,
      element
    } = context;
    const {
      parent: parentScope
    } = scope;
    return this._simulator.findScopes(
      (scope2) => scope2.parent === parentScope && scope2.element !== element
    );
  };
  InclusiveGatewayBehavior.prototype._join = function(context, incomingFlowsWithToken, gatewayScopes, exclude) {
    const {
      scope
    } = context;
    const consumeScopes = incomingFlowsWithToken.map(
      (flow) => gatewayScopes.find((s) => s.initiator.element === flow)
    );
    for (const childScope of consumeScopes) {
      if (childScope !== scope) {
        this._simulator.destroyScope(childScope.complete(), scope);
      }
    }
    this._simulator.exit(context);
    exclude.push(scope);
    const stayingScopes = gatewayScopes.filter(
      (s) => !consumeScopes.includes(s)
    );
    if (stayingScopes.length) {
      this._tryJoin({
        initiator: stayingScopes[0].initiator,
        element: stayingScopes[0].element,
        scope: stayingScopes[0],
        exclude
      });
    }
  };
  InclusiveGatewayBehavior.prototype._canReachElement = function(context, targetElement, currentElement, traversed = /* @__PURE__ */ new Set()) {
    if (context.element === currentElement) {
      return false;
    }
    if (traversed.has(currentElement)) {
      return false;
    }
    traversed.add(currentElement);
    if (targetElement === currentElement) {
      return true;
    }
    if (isSequenceFlow(currentElement)) {
      return this._canReachElement(context, targetElement, currentElement.source, traversed);
    }
    if (isLinkCatch(currentElement)) {
      const linkThrowEvents = filterLinkThrowEvents(
        currentElement.parent.children,
        getLinkName(currentElement)
      );
      return linkThrowEvents.some(
        (linkThrowEvent) => this._canReachElement(context, targetElement, linkThrowEvent, traversed)
      );
    }
    const incomingFlows = filterSequenceFlows(currentElement.incoming);
    return incomingFlows.some(
      (flow) => this._canReachElement(context, targetElement, flow, traversed)
    );
  };
  function getLinkName(element) {
    return getEventDefinition(element, "bpmn:LinkEventDefinition").name;
  }
  function filterLinkThrowEvents(elements, linkName) {
    return elements.filter(
      (e2) => isLinkThrow(e2) && getLinkName(e2) === linkName
    );
  }
  InclusiveGatewayBehavior.$inject = [
    "simulator",
    "activityBehavior"
  ];

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/behaviors/ActivityBehavior.js
  function ActivityBehavior(simulator, scopeBehavior, transactionBehavior) {
    this._simulator = simulator;
    this._scopeBehavior = scopeBehavior;
    this._transactionBehavior = transactionBehavior;
    const elements = [
      "bpmn:BusinessRuleTask",
      "bpmn:CallActivity",
      "bpmn:ManualTask",
      "bpmn:ScriptTask",
      "bpmn:ServiceTask",
      "bpmn:Task",
      "bpmn:UserTask"
    ];
    for (const element of elements) {
      simulator.registerBehavior(element, this);
    }
  }
  ActivityBehavior.$inject = [
    "simulator",
    "scopeBehavior",
    "transactionBehavior"
  ];
  ActivityBehavior.prototype.signal = function(context) {
    const event2 = this._triggerMessages(context);
    if (event2) {
      return this.signalOnEvent(context, event2);
    }
    this._simulator.exit(context);
  };
  ActivityBehavior.prototype.enter = function(context) {
    const {
      element
    } = context;
    const continueEvent = this.waitAtElement(element);
    if (continueEvent) {
      return this.signalOnEvent(context, continueEvent);
    }
    const event2 = this._triggerMessages(context);
    if (event2) {
      return this.signalOnEvent(context, event2);
    }
    this._simulator.exit(context);
  };
  ActivityBehavior.prototype.exit = function(context) {
    const {
      element,
      scope
    } = context;
    const parentScope = scope.parent;
    const completing = scope.active && !scope.failed;
    if (completing && !isEventSubProcess(element)) {
      this._transactionBehavior.registerCompensation(scope);
    }
    const activatedFlows = completing ? element.outgoing.filter(isSequenceFlow) : [];
    activatedFlows.forEach(
      (element2) => this._simulator.enter({
        element: element2,
        scope: parentScope
      })
    );
    if (activatedFlows.length === 0) {
      this._scopeBehavior.tryExit(parentScope, scope);
    }
  };
  ActivityBehavior.prototype.signalOnEvent = function(context, event2) {
    const {
      scope,
      element
    } = context;
    const subscription = this._simulator.subscribe(scope, event2, (initiator) => {
      subscription.remove();
      return this._simulator.signal({
        scope,
        element,
        initiator
      });
    });
  };
  ActivityBehavior.prototype.waitAtElement = function(element) {
    const wait = this._simulator.getConfig(element).wait;
    return wait && {
      element,
      type: "continue",
      interrupting: false,
      boundary: false
    };
  };
  ActivityBehavior.prototype._getMessageContexts = function(element, after = null) {
    const filterAfter = after ? (ctx) => ctx.referencePoint.x > after.x : () => true;
    const sortByReference = (a, b) => a.referencePoint.x - b.referencePoint.x;
    return [
      ...element.incoming.filter(isMessageFlow).map((flow) => ({
        incoming: flow,
        referencePoint: last(flow.waypoints)
      })),
      ...element.outgoing.filter(isMessageFlow).map((flow) => ({
        outgoing: flow,
        referencePoint: first(flow.waypoints)
      }))
    ].sort(sortByReference).filter(filterAfter);
  };
  ActivityBehavior.prototype._triggerMessages = function(context) {
    const {
      element,
      initiator,
      scope
    } = context;
    let messageContexts = scope.messageContexts;
    if (!messageContexts) {
      messageContexts = scope.messageContexts = this._getMessageContexts(element);
    }
    const initiatingFlow = initiator && initiator.element;
    if (isMessageFlow(initiatingFlow)) {
      if (scope.expectedIncoming !== initiatingFlow) {
        console.debug("Simulator :: ActivityBehavior :: ignoring out-of-bounds message");
        return;
      }
    }
    while (messageContexts.length) {
      const {
        incoming,
        outgoing
      } = messageContexts.shift();
      if (incoming) {
        if (!initiator) {
          continue;
        }
        scope.expectedIncoming = incoming;
        return {
          element,
          type: "message",
          name: incoming.id,
          interrupting: false,
          boundary: false
        };
      }
      this._simulator.signal({
        element: outgoing
      });
    }
  };
  function first(arr) {
    return arr && arr[0];
  }
  function last(arr) {
    return arr && arr[arr.length - 1];
  }

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/behaviors/SubProcessBehavior.js
  function SubProcessBehavior(simulator, activityBehavior, scopeBehavior, transactionBehavior, elementRegistry) {
    this._simulator = simulator;
    this._activityBehavior = activityBehavior;
    this._scopeBehavior = scopeBehavior;
    this._transactionBehavior = transactionBehavior;
    this._elementRegistry = elementRegistry;
    simulator.registerBehavior("bpmn:SubProcess", this);
    simulator.registerBehavior("bpmn:Transaction", this);
    simulator.registerBehavior("bpmn:AdHocSubProcess", this);
  }
  SubProcessBehavior.$inject = [
    "simulator",
    "activityBehavior",
    "scopeBehavior",
    "transactionBehavior",
    "elementRegistry"
  ];
  SubProcessBehavior.prototype.signal = function(context) {
    this._start(context);
  };
  SubProcessBehavior.prototype.enter = function(context) {
    const {
      element
    } = context;
    const continueEvent = this._activityBehavior.waitAtElement(element);
    if (continueEvent) {
      return this._activityBehavior.signalOnEvent(context, continueEvent);
    }
    this._start(context);
  };
  SubProcessBehavior.prototype.exit = function(context) {
    const {
      scope
    } = context;
    const parentScope = scope.parent;
    if (parentScope.failInitiator === scope) {
      parentScope.complete();
    }
    this._activityBehavior.exit(context);
  };
  SubProcessBehavior.prototype._start = function(context) {
    const {
      element,
      startEvent,
      scope
    } = context;
    const targetScope = scope.parent;
    if (isEventSubProcess(element)) {
      if (!startEvent) {
        throw new Error("missing <startEvent>: required for event sub-process");
      }
    } else {
      if (startEvent) {
        throw new Error("unexpected <startEvent>: not allowed for sub-process");
      }
    }
    if (targetScope.destroyed) {
      throw new Error(`target scope <${targetScope.id}> destroyed`);
    }
    if (isTransaction(element)) {
      this._transactionBehavior.setup(context);
    }
    if (startEvent && isInterrupting(startEvent)) {
      this._scopeBehavior.interrupt(targetScope, scope);
    }
    const startNodes = this._findStarts(element, startEvent);
    for (const element2 of startNodes) {
      if (isStartEvent(element2)) {
        this._simulator.signal({
          element: element2,
          parentScope: scope,
          initiator: scope
        });
      } else {
        this._simulator.enter({
          element: element2,
          scope,
          initiator: scope
        });
      }
    }
    if (!startNodes.length) {
      this._simulator.exit(context);
    }
  };
  SubProcessBehavior.prototype._findStarts = function(element, startEvent) {
    const isStartEvent2 = startEvent ? (node) => startEvent === node : (node) => isNoneStartEvent(node);
    return getChildren(element, this._elementRegistry).filter(
      (node) => isStartEvent2(node) || isImplicitStartEvent(node)
    );
  };
  function isTransaction(element) {
    return is(element, "bpmn:Transaction");
  }

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/behaviors/TransactionBehavior.js
  var CANCEL_EVENT = {
    type: "cancel",
    interrupting: true,
    boundary: false,
    persistent: true
  };
  function TransactionBehavior(simulator, scopeBehavior, elementRegistry) {
    this._simulator = simulator;
    this._scopeBehavior = scopeBehavior;
    this._elementRegistry = elementRegistry;
  }
  TransactionBehavior.$inject = [
    "simulator",
    "scopeBehavior",
    "elementRegistry"
  ];
  TransactionBehavior.prototype.setup = function(context) {
    const {
      scope
    } = context;
    const cancelSubscription = this._simulator.subscribe(scope, CANCEL_EVENT, (initiator) => {
      cancelSubscription.remove();
      return this.cancel({
        scope,
        initiator
      });
    });
    const compensateEvent = {
      type: "compensate",
      ref: scope.element,
      persistent: true,
      traits: ScopeTraits.NOT_DEAD
    };
    const compensateSubscription = this._simulator.subscribe(scope, compensateEvent, (initiator) => {
      if (!scope.canceled) {
        return this._simulator.trigger({
          event: CANCEL_EVENT,
          scope
        });
      }
      compensateSubscription.remove();
      return this.compensate({
        scope,
        element: scope.element,
        initiator
      });
    });
  };
  TransactionBehavior.prototype.cancel = function(context) {
    const {
      scope,
      initiator
    } = context;
    if (scope.destroyed) {
      return;
    }
    scope.cancel(initiator);
    this._simulator.trigger({
      event: {
        type: "compensate",
        ref: scope.element
      },
      initiator,
      scope
    });
    return this._simulator.trigger({
      scope,
      initiator,
      event: CANCEL_EVENT
    });
  };
  TransactionBehavior.prototype.registerCompensation = function(scope) {
    const {
      element
    } = scope;
    const children = getChildren(element, this._elementRegistry);
    const compensateStartEvents = children.filter(
      isEventSubProcess
    ).map(
      (element2) => getChildren(element2, this._elementRegistry).find(
        (element3) => isStartEvent(element3) && isCompensationEvent(element3)
      )
    ).filter((s) => s);
    const compensateBoundaryEvents = element.attachers.filter(isCompensationEvent);
    if (!compensateStartEvents.length && !compensateBoundaryEvents.length) {
      return;
    }
    const transactionScope = this.findTransactionScope(scope);
    if (!is(transactionScope.element, "bpmn:Transaction")) {
      this.makeCompensable(transactionScope);
    }
    for (const startEvent of compensateStartEvents) {
      const compensationEvent = {
        element: startEvent,
        type: "compensate",
        persistent: true,
        interrupting: true,
        ref: element,
        traits: ScopeTraits.NOT_DEAD
      };
      const compensateEventSub = startEvent.parent;
      const subscription = this._simulator.subscribe(scope, compensationEvent, (initiator) => {
        subscription.remove();
        return this._simulator.signal({
          initiator,
          element: compensateEventSub,
          startEvent,
          parentScope: scope
        });
      });
    }
    for (const boundaryEvent of compensateBoundaryEvents) {
      const compensationEvent = {
        element: boundaryEvent,
        type: "compensate",
        persistent: true,
        ref: element,
        traits: ScopeTraits.NOT_DEAD
      };
      const compensateActivity = boundaryEvent.outgoing.map(
        (outgoing) => outgoing.target
      ).find(
        isCompensationActivity
      );
      if (!compensateActivity) {
        continue;
      }
      const subscription = this._simulator.subscribe(transactionScope, compensationEvent, (initiator) => {
        subscription.remove();
        return this._simulator.enter({
          initiator,
          element: compensateActivity,
          scope: transactionScope
        });
      });
    }
  };
  TransactionBehavior.prototype.makeCompensable = function(scope) {
    if (scope.hasTrait(ScopeTraits.COMPENSABLE) || !scope.parent) {
      return;
    }
    const compensateEvent = {
      type: "compensate",
      ref: scope.element,
      interrupting: true,
      persistent: true,
      traits: ScopeTraits.NOT_DEAD
    };
    scope.compensable();
    const scopeSub = this._simulator.subscribe(scope, compensateEvent, (initiator) => {
      scopeSub.remove();
      scope.fail(initiator);
      this.compensate({
        scope,
        element: scope.element,
        initiator
      });
      this._scopeBehavior.tryExit(scope, initiator);
      return scope;
    });
    const parentScope = scope.parent;
    if (!parentScope) {
      return;
    }
    const parentSub = this._simulator.subscribe(parentScope, compensateEvent, (initiator) => {
      parentSub.remove();
      return this._simulator.trigger({
        scope,
        event: compensateEvent,
        initiator
      });
    });
    this.makeCompensable(parentScope);
  };
  TransactionBehavior.prototype.findTransactionScope = function(scope) {
    let parentScope = scope;
    while (parentScope) {
      const element = parentScope.element;
      if (is(element, "bpmn:SubProcess") && !isEventSubProcess(element)) {
        return parentScope;
      }
      if (isAny2(element, [
        "bpmn:Transaction",
        "bpmn:Process",
        "bpmn:Participant"
      ])) {
        return parentScope;
      }
      parentScope = parentScope.parent;
    }
    throw noTransactionContext(scope);
  };
  TransactionBehavior.prototype.compensate = function(context) {
    const {
      scope,
      element
    } = context;
    const compensateSubscriptions = filterSet(
      scope.subscriptions,
      (subscription) => eventsMatch({ type: "compensate" }, subscription.event)
    );
    const localSubscriptions = compensateSubscriptions.filter((subscription) => subscription.event.ref === element);
    const otherSubscriptions = compensateSubscriptions.filter((subscription) => subscription.event.ref !== element);
    for (const subscription of localSubscriptions) {
      this._scopeBehavior.preExit(scope, (initiator) => {
        return this._simulator.trigger(subscription);
      });
    }
    for (const subscription of otherSubscriptions.reverse()) {
      this._scopeBehavior.preExit(scope, (initiator) => {
        return this._simulator.trigger(subscription);
      });
    }
  };
  function noTransactionContext(scope) {
    throw new Error(`no transaction context for <${scope.id}>`);
  }

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/behaviors/SequenceFlowBehavior.js
  function SequenceFlowBehavior(simulator, scopeBehavior) {
    this._simulator = simulator;
    this._scopeBehavior = scopeBehavior;
    simulator.registerBehavior("bpmn:SequenceFlow", this);
  }
  SequenceFlowBehavior.prototype.enter = function(context) {
    this._simulator.exit(context);
  };
  SequenceFlowBehavior.prototype.exit = function(context) {
    const {
      element,
      scope
    } = context;
    this._simulator.enter({
      initiator: scope,
      element: element.target,
      scope: scope.parent
    });
  };
  SequenceFlowBehavior.$inject = [
    "simulator",
    "scopeBehavior"
  ];

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/behaviors/MessageFlowBehavior.js
  function MessageFlowBehavior(simulator) {
    this._simulator = simulator;
    simulator.registerBehavior("bpmn:MessageFlow", this);
  }
  MessageFlowBehavior.$inject = ["simulator"];
  MessageFlowBehavior.prototype.signal = function(context) {
    this._simulator.exit(context);
  };
  MessageFlowBehavior.prototype.exit = function(context) {
    const {
      element,
      scope: initiator
    } = context;
    const target = element.target;
    const event2 = isCatchEvent(target) ? target : {
      type: "message",
      element,
      name: element.id
    };
    const subscription = this._simulator.findSubscription({
      event: event2,
      elements: [target, target.parent]
    });
    if (subscription) {
      this._simulator.trigger({
        event: event2,
        initiator,
        scope: subscription.scope
      });
    }
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/behaviors/EventBehaviors.js
  function EventBehaviors(simulator, elementRegistry, scopeBehavior) {
    this._simulator = simulator;
    this._elementRegistry = elementRegistry;
    this._scopeBehavior = scopeBehavior;
  }
  EventBehaviors.$inject = [
    "simulator",
    "elementRegistry",
    "scopeBehavior"
  ];
  EventBehaviors.prototype.get = function(element) {
    const behaviors = {
      "bpmn:LinkEventDefinition": (context) => {
        const {
          element: element2,
          scope
        } = context;
        const link = getLinkDefinition(element2);
        const parentScope = scope.parent;
        const parentElement = parentScope.element;
        const children = getChildren(parentElement, this._elementRegistry);
        const linkTargets = children.filter(
          (element3) => isLinkCatch(element3) && getLinkDefinition(element3).name === link.name
        );
        for (const linkTarget of linkTargets) {
          this._simulator.signal({
            element: linkTarget,
            parentScope,
            initiator: scope
          });
        }
      },
      "bpmn:SignalEventDefinition": (context) => {
        const {
          element: element2,
          scope
        } = context;
        const subscriptions = this._simulator.findSubscriptions({
          event: element2
        });
        const signaledScopes = /* @__PURE__ */ new Set();
        for (const subscription of subscriptions) {
          const signaledScope = subscription.scope;
          if (signaledScopes.has(signaledScope)) {
            continue;
          }
          signaledScopes.add(signaledScope);
          this._simulator.trigger({
            event: element2,
            scope: signaledScope,
            initiator: scope
          });
        }
      },
      "bpmn:EscalationEventDefinition": (context) => {
        const {
          element: element2,
          scope
        } = context;
        const scopes = this._simulator.findScopes({
          subscribedTo: {
            event: element2
          },
          trait: ScopeTraits.ACTIVE
        });
        let triggerScope = scope;
        while (triggerScope = triggerScope.parent) {
          if (scopes.includes(triggerScope)) {
            this._simulator.trigger({
              event: element2,
              scope: triggerScope,
              initiator: scope
            });
            break;
          }
        }
      },
      "bpmn:ErrorEventDefinition": (context) => {
        const {
          element: element2,
          scope
        } = context;
        const scopes = this._simulator.findScopes({
          subscribedTo: {
            event: element2
          },
          trait: ScopeTraits.ACTIVE
        });
        let triggerScope = scope;
        while (triggerScope = triggerScope.parent) {
          if (scopes.includes(triggerScope)) {
            this._simulator.trigger({
              event: element2,
              scope: triggerScope,
              initiator: scope
            });
            break;
          }
        }
      },
      "bpmn:TerminateEventDefinition": (context) => {
        const {
          scope
        } = context;
        this._scopeBehavior.terminate(scope.parent, scope);
      },
      "bpmn:CancelEventDefinition": (context) => {
        const {
          scope,
          element: element2
        } = context;
        this._simulator.trigger({
          event: element2,
          initiator: scope,
          scope: findSubscriptionScope(scope)
        });
      },
      "bpmn:CompensateEventDefinition": (context) => {
        const {
          scope,
          element: element2
        } = context;
        return this._simulator.waitForScopes(
          scope,
          this._simulator.trigger({
            event: element2,
            scope: findSubscriptionScope(scope)
          })
        );
      }
    };
    const entry = Object.entries(behaviors).find(
      (entry2) => isTypedEvent2(element, entry2[0])
    );
    return entry && entry[1];
  };
  function getLinkDefinition(element) {
    return getEventDefinition(element, "bpmn:LinkEventDefinition");
  }
  function findSubscriptionScope(scope) {
    while (isEventSubProcess(scope.parent.element)) {
      scope = scope.parent;
    }
    return scope.parent;
  }

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/behaviors/ScopeBehavior.js
  var PRE_EXIT_EVENT = {
    type: "pre-exit",
    persistent: true,
    interrupting: true,
    boundary: false
  };
  var EXIT_EVENT = {
    type: "exit",
    interrupting: true,
    boundary: false,
    persistent: true
  };
  function ScopeBehavior(simulator) {
    this._simulator = simulator;
  }
  ScopeBehavior.$inject = [
    "simulator"
  ];
  ScopeBehavior.prototype.isFinished = function(scope, excludeScope = null) {
    excludeScope = matchScope(excludeScope);
    return scope.children.every((c) => c.destroyed || c.completed || excludeScope(c));
  };
  ScopeBehavior.prototype.destroyChildren = function(scope, initiator, excludeScope = null) {
    excludeScope = matchScope(excludeScope);
    scope.children.filter((c) => !c.destroyed && !excludeScope(c)).map((c) => {
      this._simulator.destroyScope(c, initiator);
    });
  };
  ScopeBehavior.prototype.terminate = function(scope, initiator) {
    this.destroyChildren(scope, initiator);
    scope.terminate(initiator);
    this.tryExit(scope, initiator);
  };
  ScopeBehavior.prototype.interrupt = function(scope, initiator) {
    this.destroyChildren(scope, initiator, initiator);
    scope.fail(initiator);
  };
  ScopeBehavior.prototype.tryExit = function(scope, initiator) {
    if (!scope) {
      throw new Error("missing <scope>");
    }
    if (!initiator) {
      initiator = scope;
    }
    if (!this.isFinished(scope, initiator)) {
      return EXIT_EVENT;
    }
    const preExitSubscriptions = this._simulator.findSubscriptions({
      event: PRE_EXIT_EVENT,
      scope
    });
    for (const subscription of preExitSubscriptions) {
      const {
        event: event2,
        scope: scope2
      } = subscription;
      const scopes = this._simulator.trigger({
        event: event2,
        scope: scope2,
        initiator
      });
      if (scopes.length) {
        return EXIT_EVENT;
      }
    }
    this._simulator.trigger({
      event: EXIT_EVENT,
      scope,
      initiator
    });
    this.exit({
      scope,
      initiator
    });
  };
  ScopeBehavior.prototype.exit = function(context) {
    const {
      scope,
      initiator
    } = context;
    if (!initiator) {
      throw new Error("missing <initiator>");
    }
    this._simulator.exit({
      element: scope.element,
      scope,
      initiator
    });
  };
  ScopeBehavior.prototype.preExit = function(scope, triggerFn) {
    const subscription = this._simulator.subscribe(scope, PRE_EXIT_EVENT, (initiator) => {
      subscription.remove();
      return triggerFn(initiator);
    });
    return subscription;
  };
  function matchScope(fnOrScope) {
    if (typeof fnOrScope === "function") {
      return fnOrScope;
    }
    return (scope) => scope === fnOrScope;
  }

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/behaviors/ProcessBehavior.js
  function ProcessBehavior(simulator, scopeBehavior) {
    this._simulator = simulator;
    this._scopeBehavior = scopeBehavior;
    simulator.registerBehavior("bpmn:Process", this);
    simulator.registerBehavior("bpmn:Participant", this);
  }
  ProcessBehavior.prototype.signal = function(context) {
    const {
      element,
      startEvent,
      startNodes = this._findStarts(element, startEvent),
      scope
    } = context;
    if (!startNodes.length) {
      throw new Error("missing <startNodes> or <startEvent>");
    }
    for (const startNode of startNodes) {
      if (isStartEvent(startNode)) {
        this._simulator.signal({
          element: startNode,
          parentScope: scope
        });
      } else {
        this._simulator.enter({
          element: startNode,
          scope
        });
      }
    }
  };
  ProcessBehavior.prototype.exit = function(context) {
    const {
      scope,
      initiator
    } = context;
    this._scopeBehavior.destroyChildren(scope, initiator);
  };
  ProcessBehavior.prototype._findStarts = function(element, startEvent) {
    const isStartEvent2 = startEvent ? (node) => startEvent === node : (node) => isNoneStartEvent(node);
    return element.children.filter(
      (node) => isStartEvent2(node) || isImplicitStartEvent(node)
    );
  };
  ProcessBehavior.$inject = [
    "simulator",
    "scopeBehavior"
  ];

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/behaviors/index.js
  var behaviors_default = {
    __init__: [
      "startEventBehavior",
      "endEventBehavior",
      "boundaryEventBehavior",
      "intermediateCatchEventBehavior",
      "intermediateThrowEventBehavior",
      "exclusiveGatewayBehavior",
      "parallelGatewayBehavior",
      "eventBasedGatewayBehavior",
      "inclusiveGatewayBehavior",
      "subProcessBehavior",
      "sequenceFlowBehavior",
      "messageFlowBehavior",
      "processBehavior"
    ],
    startEventBehavior: ["type", StartEventBehavior],
    endEventBehavior: ["type", EndEventBehavior],
    boundaryEventBehavior: ["type", BoundaryEventBehavior],
    intermediateCatchEventBehavior: ["type", IntermediateCatchEventBehavior],
    intermediateThrowEventBehavior: ["type", IntermediateThrowEventBehavior],
    exclusiveGatewayBehavior: ["type", ExclusiveGatewayBehavior],
    parallelGatewayBehavior: ["type", ParallelGatewayBehavior],
    eventBasedGatewayBehavior: ["type", EventBasedGatewayBehavior],
    inclusiveGatewayBehavior: ["type", InclusiveGatewayBehavior],
    activityBehavior: ["type", ActivityBehavior],
    subProcessBehavior: ["type", SubProcessBehavior],
    sequenceFlowBehavior: ["type", SequenceFlowBehavior],
    messageFlowBehavior: ["type", MessageFlowBehavior],
    eventBehaviors: ["type", EventBehaviors],
    scopeBehavior: ["type", ScopeBehavior],
    processBehavior: ["type", ProcessBehavior],
    transactionBehavior: ["type", TransactionBehavior]
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/simulator/index.js
  var HIGH_PRIORITY = 5e3;
  var simulator_default = {
    __depends__: [
      behaviors_default
    ],
    __init__: [
      ["eventBus", "simulator", function(eventBus, simulator) {
        eventBus.on([
          "tokenSimulation.toggleMode",
          "tokenSimulation.resetSimulation"
        ], HIGH_PRIORITY, (event2) => {
          simulator.reset();
        });
      }]
    ],
    simulator: ["type", Simulator]
  };

  // ../../node_modules/inherits-browser/dist/index.es.js
  function e(e2, t) {
    t && (e2.super_ = t, e2.prototype = Object.create(t.prototype, { constructor: { value: e2, enumerable: false, writable: true, configurable: true } }));
  }

  // ../../node_modules/bpmn-js-token-simulation/lib/animation/behaviors/AnimatedMessageFlowBehavior.js
  function AnimatedMessageFlowBehavior(injector, animation) {
    injector.invoke(MessageFlowBehavior, this);
    this._animation = animation;
  }
  e(AnimatedMessageFlowBehavior, MessageFlowBehavior);
  AnimatedMessageFlowBehavior.$inject = [
    "injector",
    "animation"
  ];
  AnimatedMessageFlowBehavior.prototype.signal = function(context) {
    const {
      element,
      scope
    } = context;
    this._animation.animate(element, scope, () => {
      MessageFlowBehavior.prototype.signal.call(this, context);
    });
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/animation/behaviors/AnimatedSequenceFlowBehavior.js
  function AnimatedSequenceFlowBehavior(injector, animation) {
    injector.invoke(SequenceFlowBehavior, this);
    this._animation = animation;
  }
  e(AnimatedSequenceFlowBehavior, SequenceFlowBehavior);
  AnimatedSequenceFlowBehavior.$inject = [
    "injector",
    "animation"
  ];
  AnimatedSequenceFlowBehavior.prototype.enter = function(context) {
    const {
      element,
      scope
    } = context;
    this._animation.animate(element, scope, () => {
      SequenceFlowBehavior.prototype.enter.call(this, context);
    });
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/animation/behaviors/index.js
  var behaviors_default2 = {
    sequenceFlowBehavior: ["type", AnimatedSequenceFlowBehavior],
    messageFlowBehavior: ["type", AnimatedMessageFlowBehavior]
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/features/scope-filter/ScopeFilter.js
  var DEFAULT_SCOPE_FILTER = (s) => true;
  function ScopeFilter(eventBus, simulator) {
    this._eventBus = eventBus;
    this._simulator = simulator;
    this._filter = DEFAULT_SCOPE_FILTER;
    eventBus.on([
      TOGGLE_MODE_EVENT,
      RESET_SIMULATION_EVENT
    ], () => {
      this._filter = DEFAULT_SCOPE_FILTER;
    });
    eventBus.on(SCOPE_DESTROYED_EVENT, (event2) => {
      const {
        scope
      } = event2;
      if (this._scope === scope && scope.parent) {
        this.toggle(scope.parent);
      }
    });
    eventBus.on(SCOPE_CREATE_EVENT, (event2) => {
      const {
        scope
      } = event2;
      if (!scope.parent && this._scope && !isAncestor(this._scope, scope)) {
        this.toggle(null);
      }
    });
  }
  ScopeFilter.prototype.toggle = function(scope) {
    const setFilter = this._scope !== scope;
    this._scope = setFilter ? scope : null;
    this._filter = this._scope ? (s) => isAncestor(this._scope, s) : (s) => true;
    this._eventBus.fire(SCOPE_FILTER_CHANGED_EVENT, {
      filter: this._filter,
      scope: this._scope
    });
  };
  ScopeFilter.prototype.isShown = function(scope) {
    if (typeof scope === "string") {
      scope = this._simulator.findScope((s) => s.id === scope);
    }
    return scope && this._filter(scope);
  };
  ScopeFilter.prototype.isFocused = function(scope) {
    const id = scope.id || scope;
    return this._scope?.id === id;
  };
  ScopeFilter.prototype.findScope = function(options) {
    return this._simulator.findScopes(options).filter((s) => this.isShown(s))[0];
  };
  ScopeFilter.$inject = [
    "eventBus",
    "simulator"
  ];
  function isAncestor(parent, scope) {
    do {
      if (parent === scope) {
        return true;
      }
    } while (scope = scope.parent);
    return false;
  }

  // ../../node_modules/bpmn-js-token-simulation/lib/features/scope-filter/index.js
  var scope_filter_default = {
    scopeFilter: ["type", ScopeFilter]
  };

  // ../../node_modules/tiny-svg/dist/index.js
  function ensureImported(element, target) {
    if (element.ownerDocument !== target.ownerDocument) {
      try {
        return target.ownerDocument.importNode(element, true);
      } catch (e2) {
      }
    }
    return element;
  }
  function appendTo(element, target) {
    return target.appendChild(ensureImported(element, target));
  }
  var LENGTH_ATTR = 2;
  var CSS_PROPERTIES = {
    "alignment-baseline": 1,
    "baseline-shift": 1,
    "clip": 1,
    "clip-path": 1,
    "clip-rule": 1,
    "color": 1,
    "color-interpolation": 1,
    "color-interpolation-filters": 1,
    "color-profile": 1,
    "color-rendering": 1,
    "cursor": 1,
    "direction": 1,
    "display": 1,
    "dominant-baseline": 1,
    "enable-background": 1,
    "fill": 1,
    "fill-opacity": 1,
    "fill-rule": 1,
    "filter": 1,
    "flood-color": 1,
    "flood-opacity": 1,
    "font": 1,
    "font-family": 1,
    "font-size": LENGTH_ATTR,
    "font-size-adjust": 1,
    "font-stretch": 1,
    "font-style": 1,
    "font-variant": 1,
    "font-weight": 1,
    "glyph-orientation-horizontal": 1,
    "glyph-orientation-vertical": 1,
    "image-rendering": 1,
    "kerning": 1,
    "letter-spacing": 1,
    "lighting-color": 1,
    "marker": 1,
    "marker-end": 1,
    "marker-mid": 1,
    "marker-start": 1,
    "mask": 1,
    "opacity": 1,
    "overflow": 1,
    "pointer-events": 1,
    "shape-rendering": 1,
    "stop-color": 1,
    "stop-opacity": 1,
    "stroke": 1,
    "stroke-dasharray": 1,
    "stroke-dashoffset": 1,
    "stroke-linecap": 1,
    "stroke-linejoin": 1,
    "stroke-miterlimit": 1,
    "stroke-opacity": 1,
    "stroke-width": LENGTH_ATTR,
    "text-anchor": 1,
    "text-decoration": 1,
    "text-rendering": 1,
    "unicode-bidi": 1,
    "visibility": 1,
    "word-spacing": 1,
    "writing-mode": 1
  };
  function getAttribute(node, name) {
    if (CSS_PROPERTIES[name]) {
      return node.style[name];
    } else {
      return node.getAttributeNS(null, name);
    }
  }
  function setAttribute(node, name, value) {
    var hyphenated = name.replace(/([a-z])([A-Z])/g, "$1-$2").toLowerCase();
    var type = CSS_PROPERTIES[hyphenated];
    if (type) {
      if (type === LENGTH_ATTR && typeof value === "number") {
        value = String(value) + "px";
      }
      node.style[hyphenated] = value;
    } else {
      node.setAttributeNS(null, name, value);
    }
  }
  function setAttributes(node, attrs) {
    var names = Object.keys(attrs), i, name;
    for (i = 0, name; name = names[i]; i++) {
      setAttribute(node, name, attrs[name]);
    }
  }
  function attr(node, name, value) {
    if (typeof name === "string") {
      if (value !== void 0) {
        setAttribute(node, name, value);
      } else {
        return getAttribute(node, name);
      }
    } else {
      setAttributes(node, name);
    }
    return node;
  }
  var toString2 = Object.prototype.toString;
  function ClassList2(el) {
    if (!el || !el.nodeType) {
      throw new Error("A DOM element reference is required");
    }
    this.el = el;
    this.list = el.classList;
  }
  ClassList2.prototype.add = function(name) {
    this.list.add(name);
    return this;
  };
  ClassList2.prototype.remove = function(name) {
    if ("[object RegExp]" == toString2.call(name)) {
      return this.removeMatching(name);
    }
    this.list.remove(name);
    return this;
  };
  ClassList2.prototype.removeMatching = function(re) {
    const arr = this.array();
    for (let i = 0; i < arr.length; i++) {
      if (re.test(arr[i])) {
        this.remove(arr[i]);
      }
    }
    return this;
  };
  ClassList2.prototype.toggle = function(name, force) {
    if ("undefined" !== typeof force) {
      if (force !== this.list.toggle(name, force)) {
        this.list.toggle(name);
      }
    } else {
      this.list.toggle(name);
    }
    return this;
  };
  ClassList2.prototype.array = function() {
    return Array.from(this.list);
  };
  ClassList2.prototype.has = ClassList2.prototype.contains = function(name) {
    return this.list.contains(name);
  };
  var ns = {
    svg: "http://www.w3.org/2000/svg"
  };
  var SVG_START = '<svg xmlns="' + ns.svg + '"';
  function parse(svg) {
    var unwrap = false;
    if (svg.substring(0, 4) === "<svg") {
      if (svg.indexOf(ns.svg) === -1) {
        svg = SVG_START + svg.substring(4);
      }
    } else {
      svg = SVG_START + ">" + svg + "</svg>";
      unwrap = true;
    }
    var parsed = parseDocument(svg);
    if (!unwrap) {
      return parsed;
    }
    var fragment = document.createDocumentFragment();
    var parent = parsed.firstChild;
    while (parent.firstChild) {
      fragment.appendChild(parent.firstChild);
    }
    return fragment;
  }
  function parseDocument(svg) {
    var parser;
    parser = new DOMParser();
    parser.async = false;
    return parser.parseFromString(svg, "text/xml");
  }
  function create(name, attrs) {
    var element;
    name = name.trim();
    if (name.charAt(0) === "<") {
      element = parse(name).firstChild;
      element = document.importNode(element, true);
    } else {
      element = document.createElementNS(ns.svg, name);
    }
    if (attrs) {
      attr(element, attrs);
    }
    return element;
  }
  function remove(element) {
    var parent = element.parentNode;
    if (parent) {
      parent.removeChild(element);
    }
    return element;
  }

  // ../../node_modules/bpmn-js-token-simulation/lib/animation/Animation.js
  var STYLE = getComputedStyle(document.documentElement);
  var DEFAULT_PRIMARY_COLOR = STYLE.getPropertyValue("--token-simulation-green-base-44");
  var DEFAULT_AUXILIARY_COLOR = STYLE.getPropertyValue("--token-simulation-white");
  function noop() {
  }
  function getSegmentEasing(index2, waypoints) {
    if (waypoints.length === 2) {
      return EASE_IN_OUT;
    }
    if (index2 === 1) {
      return EASE_IN;
    }
    if (index2 === waypoints.length - 1) {
      return EASE_OUT;
    }
    return EASE_LINEAR;
  }
  var EASE_LINEAR = function(pos) {
    return pos;
  };
  var EASE_IN = function(pos) {
    return -Math.cos(pos * Math.PI / 2) + 1;
  };
  var EASE_OUT = function(pos) {
    return Math.sin(pos * Math.PI / 2);
  };
  var EASE_IN_OUT = function(pos) {
    return -Math.cos(pos * Math.PI) / 2 + 0.5;
  };
  var TOKEN_SIZE = 20;
  function Animation(config, canvas, eventBus, scopeFilter) {
    this._eventBus = eventBus;
    this._scopeFilter = scopeFilter;
    this._canvas = canvas;
    this._randomize = config && config.randomize !== false;
    this._animations = /* @__PURE__ */ new Set();
    this._speed = 1;
    eventBus.on([
      "diagram.destroy",
      RESET_SIMULATION_EVENT
    ], () => {
      this.clearAnimations();
    });
    eventBus.on(PAUSE_SIMULATION_EVENT, () => {
      this.pause();
    });
    eventBus.on(PLAY_SIMULATION_EVENT, () => {
      this.play();
    });
    eventBus.on(SCOPE_FILTER_CHANGED_EVENT, (event2) => {
      this.each((animation) => {
        if (this._scopeFilter.isShown(animation.scope)) {
          animation.show();
        } else {
          animation.hide();
        }
      });
    });
    eventBus.on(SCOPE_DESTROYED_EVENT, (event2) => {
      const {
        scope
      } = event2;
      this.clearAnimations(scope);
    });
  }
  Animation.prototype.animate = function(connection, scope, done) {
    this.createAnimation(connection, scope, done);
  };
  Animation.prototype.pause = function() {
    this.each((animation) => animation.pause());
  };
  Animation.prototype.play = function() {
    this.each((animation) => animation.play());
  };
  Animation.prototype.each = function(fn) {
    this._animations.forEach(fn);
  };
  Animation.prototype.createAnimation = function(connection, scope, done = noop) {
    const group = this._getGroup(scope);
    if (!group) {
      return;
    }
    const tokenGfx = this._createTokenGfx(group, scope);
    const animation = new TokenAnimation(tokenGfx, connection.waypoints, this._randomize, () => {
      this._clearAnimation(animation);
      done();
    });
    animation.setSpeed(this.getAnimationSpeed());
    if (!this._scopeFilter.isShown(scope)) {
      animation.hide();
    }
    animation.scope = scope;
    animation.element = connection;
    this._animations.add(animation);
    this._eventBus.fire(ANIMATION_CREATED_EVENT, {
      animation
    });
    animation.play();
    return animation;
  };
  Animation.prototype.setAnimationSpeed = function(speed) {
    this._speed = speed;
    this.each((animation) => animation.setSpeed(speed));
    this._eventBus.fire(ANIMATION_SPEED_CHANGED_EVENT, {
      speed
    });
  };
  Animation.prototype.getAnimationSpeed = function() {
    return this._speed;
  };
  Animation.prototype.clearAnimations = function(scope) {
    this.each((animation) => {
      if (!scope || animation.scope === scope) {
        this._clearAnimation(animation);
      }
    });
  };
  Animation.prototype._clearAnimation = function(animation) {
    animation.remove();
    this._animations.delete(animation);
  };
  Animation.prototype._createTokenGfx = function(group, scope) {
    const parent = create(this._getTokenSVG(scope).trim());
    return appendTo(parent, group);
  };
  Animation.prototype._getTokenSVG = function(scope) {
    const colors = scope.colors || {
      primary: DEFAULT_PRIMARY_COLOR,
      auxiliary: DEFAULT_AUXILIARY_COLOR
    };
    return `
    <g class="bts-token">
      <circle
        class="bts-circle"
        r="${TOKEN_SIZE / 2}"
        cx="${TOKEN_SIZE / 2}"
        cy="${TOKEN_SIZE / 2}"
        fill="${colors.primary}"
      />
      <text
        class="bts-text"
        transform="translate(10, 14)"
        text-anchor="middle"
        fill="${colors.auxiliary}"
      >1</text>
    </g>
  `;
  };
  Animation.prototype._getGroup = function(scope) {
    var canvas = this._canvas;
    var layer, root;
    if ("findRoot" in canvas) {
      root = canvas.findRoot(scope.element);
      layer = canvas._findPlaneForRoot(root).layer;
    } else {
      layer = query(".viewport", canvas._svg);
    }
    var group = query(".bts-animation-tokens", layer);
    if (!group) {
      group = create('<g class="bts-animation-tokens" />');
      appendTo(
        group,
        layer
      );
    }
    return group;
  };
  Animation.$inject = [
    "config.animation",
    "canvas",
    "eventBus",
    "scopeFilter"
  ];
  function TokenAnimation(gfx, waypoints, randomize, done) {
    this.gfx = gfx;
    this.waypoints = waypoints;
    this.done = done;
    this.randomize = randomize;
    this._paused = true;
    this._t = 0;
    this._parts = [];
    this.create();
  }
  TokenAnimation.prototype.pause = function() {
    this._paused = true;
  };
  TokenAnimation.prototype.play = function() {
    if (this._paused) {
      this._paused = false;
      this.tick(0);
    }
    this.schedule();
  };
  TokenAnimation.prototype.schedule = function() {
    if (this._paused) {
      return;
    }
    if (this._scheduled) {
      return;
    }
    const last2 = Date.now();
    this._scheduled = true;
    requestAnimationFrame(() => {
      this._scheduled = false;
      if (this._paused) {
        return;
      }
      this.tick((Date.now() - last2) * this._speed);
      this.schedule();
    });
  };
  TokenAnimation.prototype.tick = function(tElapsed) {
    const t = this._t = this._t + tElapsed;
    const part = this._parts.find(
      (p) => p.startTime <= t && p.endTime > t
    );
    if (!part) {
      return this.completed();
    }
    const segmentTime = t - part.startTime;
    const segmentLength = part.length * part.easing(segmentTime / part.duration);
    const currentLength = part.startLength + segmentLength;
    const point = this._path.getPointAtLength(currentLength);
    this.move(point.x, point.y);
  };
  TokenAnimation.prototype.move = function(x, y) {
    attr(this.gfx, "transform", `translate(${x}, ${y})`);
  };
  TokenAnimation.prototype.create = function() {
    const waypoints = this.waypoints;
    const parts = waypoints.reduce((parts2, point, index2) => {
      const lastPoint = waypoints[index2 - 1];
      if (lastPoint) {
        const lastPart = parts2[parts2.length - 1];
        const startLength = lastPart && lastPart.endLength || 0;
        const length = distance(lastPoint, point);
        parts2.push({
          startLength,
          endLength: startLength + length,
          length,
          easing: getSegmentEasing(index2, waypoints)
        });
      }
      return parts2;
    }, []);
    const totalLength = parts.reduce(function(length, part) {
      return length + part.length;
    }, 0);
    const d = waypoints.reduce((d2, waypoint, index2) => {
      const x = waypoint.x - TOKEN_SIZE / 2, y = waypoint.y - TOKEN_SIZE / 2;
      d2.push([index2 > 0 ? "L" : "M", x, y]);
      return d2;
    }, []).flat().join(" ");
    const totalDuration = getAnimationDuration(totalLength, this._randomize);
    this._parts = parts.reduce((parts2, part, index2) => {
      const duration = totalDuration / totalLength * part.length;
      const startTime = index2 > 0 ? parts2[index2 - 1].endTime : 0;
      const endTime = startTime + duration;
      return [
        ...parts2,
        {
          ...part,
          startTime,
          endTime,
          duration
        }
      ];
    }, []);
    this._path = create(`<path d="${d}" />`);
    this._t = 0;
  };
  TokenAnimation.prototype.show = function() {
    attr(this.gfx, "display", "");
  };
  TokenAnimation.prototype.hide = function() {
    attr(this.gfx, "display", "none");
  };
  TokenAnimation.prototype.completed = function() {
    this.done();
  };
  TokenAnimation.prototype.remove = function() {
    this.pause();
    remove(this.gfx);
  };
  TokenAnimation.prototype.setSpeed = function(speed) {
    this._speed = speed;
  };
  function getAnimationDuration(length, randomize = false) {
    return Math.log(length) * (randomize ? randomBetween(250, 300) : 250);
  }
  function randomBetween(min, max) {
    return min + Math.floor(Math.random() * (max - min));
  }
  function distance(a, b) {
    return Math.sqrt(Math.pow(a.x - b.x, 2) + Math.pow(a.y - b.y, 2));
  }

  // ../../node_modules/bpmn-js-token-simulation/lib/animation/index.js
  var animation_default = {
    __depends__: [
      simulator_default,
      behaviors_default2,
      scope_filter_default
    ],
    animation: ["type", Animation]
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/features/colored-scopes/ColoredScopes.js
  var import_randomcolor = __toESM(require_randomColor());
  var HIGH_PRIORITY2 = 1500;
  function ColoredScopes(eventBus) {
    const colors = (0, import_randomcolor.default)({
      count: 60
    }).filter((c) => getContrastYIQ(c.substring(1)) < 200);
    function getContrastYIQ(hexcolor) {
      var r = parseInt(hexcolor.substr(0, 2), 16);
      var g = parseInt(hexcolor.substr(2, 2), 16);
      var b = parseInt(hexcolor.substr(4, 2), 16);
      var yiq = (r * 299 + g * 587 + b * 114) / 1e3;
      return yiq;
    }
    let colorsIdx = 0;
    function getColors(scope) {
      const {
        element
      } = scope;
      if (element && element.type === "bpmn:MessageFlow") {
        return {
          primary: "#999",
          auxiliary: "#FFF"
        };
      }
      if (scope.parent) {
        return scope.parent.colors;
      }
      const primary = colors[colorsIdx++ % colors.length];
      return {
        primary,
        auxiliary: getContrastYIQ(primary) >= 128 ? "#111" : "#fff"
      };
    }
    eventBus.on(SCOPE_CREATE_EVENT, HIGH_PRIORITY2, (event2) => {
      const {
        scope
      } = event2;
      scope.colors = getColors(scope);
    });
  }
  ColoredScopes.$inject = [
    "eventBus"
  ];

  // ../../node_modules/bpmn-js-token-simulation/lib/features/colored-scopes/index.js
  var colored_scopes_default = {
    __init__: [
      "coloredScopes"
    ],
    coloredScopes: ["type", ColoredScopes]
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/features/context-pads/handler/ExclusiveGatewayHandler.js
  function ExclusiveGatewayHandler(exclusiveGatewaySettings) {
    this._exclusiveGatewaySettings = exclusiveGatewaySettings;
  }
  ExclusiveGatewayHandler.prototype.createContextPads = function(element) {
    const outgoingFlows = element.outgoing.filter(function(outgoing) {
      return is(outgoing, "bpmn:SequenceFlow");
    });
    if (outgoingFlows.length < 2) {
      return;
    }
    const html = `
    <button class="bts-context-pad" title="Set Sequence Flow">
      ${ForkIcon()}
    </button>
  `;
    const action = () => {
      this._exclusiveGatewaySettings.setSequenceFlow(element);
    };
    return [
      {
        action,
        element,
        html
      }
    ];
  };
  ExclusiveGatewayHandler.$inject = [
    "exclusiveGatewaySettings"
  ];

  // ../../node_modules/bpmn-js-token-simulation/lib/features/context-pads/handler/InclusiveGatewayHandler.js
  function InclusiveGatewayHandler(inclusiveGatewaySettings) {
    this._inclusiveGatewaySettings = inclusiveGatewaySettings;
  }
  InclusiveGatewayHandler.prototype.createContextPads = function(element) {
    const outgoingFlows = element.outgoing.filter(isSequenceFlow);
    if (outgoingFlows.length < 2) {
      return;
    }
    const nonDefaultFlows = outgoingFlows.filter((outgoing) => {
      const flowBo = getBusinessObject(outgoing), gatewayBo = getBusinessObject(element);
      return gatewayBo.default !== flowBo;
    });
    const html = `
    <button class="bts-context-pad" title="Set Sequence Flow">
      ${ForkIcon()}
    </button>
  `;
    return nonDefaultFlows.map((sequenceFlow) => {
      const action = () => {
        this._inclusiveGatewaySettings.toggleSequenceFlow(element, sequenceFlow);
      };
      return {
        action,
        element: sequenceFlow,
        html
      };
    });
  };
  InclusiveGatewayHandler.$inject = [
    "inclusiveGatewaySettings"
  ];

  // ../../node_modules/bpmn-js-token-simulation/lib/features/context-pads/handler/PauseHandler.js
  function PauseHandler(simulator) {
    this._simulator = simulator;
  }
  PauseHandler.prototype.createContextPads = function(element) {
    if (is(element, "bpmn:ReceiveTask") || is(element, "bpmn:SubProcess") && getBusinessObject(element).triggeredByEvent) {
      return [];
    }
    return [
      this.createPauseContextPad(element)
    ];
  };
  PauseHandler.prototype.createPauseContextPad = function(element) {
    const contexts = () => this._findSubscriptions({
      element
    });
    const wait = this._isPaused(element);
    const html = `
    <button class="bts-context-pad ${wait ? "" : "show-hover"}" title="${wait ? "Remove" : "Add"} pause point">
      ${(wait ? RemovePauseIcon : PauseIcon)("show-hover")}
      ${PauseIcon("hide-hover")}
    </button>
  `;
    const action = () => {
      this._togglePaused(element);
    };
    return {
      action,
      element,
      hideContexts: contexts,
      html
    };
  };
  PauseHandler.prototype._isPaused = function(element) {
    const {
      wait
    } = this._simulator.getConfig(element);
    return wait;
  };
  PauseHandler.prototype._togglePaused = function(element) {
    const wait = !this._isPaused(element);
    this._simulator.waitAtElement(element, wait);
  };
  PauseHandler.prototype._findSubscriptions = function(options) {
    return this._simulator.findSubscriptions(options);
  };
  PauseHandler.$inject = [
    "simulator"
  ];

  // ../../node_modules/bpmn-js-token-simulation/lib/features/context-pads/handler/TriggerHandler.js
  function TriggerHandler(simulator) {
    this._simulator = simulator;
  }
  TriggerHandler.$inject = [
    "simulator"
  ];
  TriggerHandler.prototype.createContextPads = function(element) {
    return [
      this.createTriggerContextPad(element)
    ];
  };
  TriggerHandler.prototype.createTriggerContextPad = function(element) {
    const contexts = () => {
      const subscriptions = this._findSubscriptions({
        element
      });
      const sortedSubscriptions = subscriptions.slice().sort((a, b) => {
        return a.event.type === "none" ? 1 : -1;
      });
      return sortedSubscriptions;
    };
    const html = `
    <button class="bts-context-pad" title="Trigger Event">
      ${PlayIcon()}
    </button>
  `;
    const action = (subscriptions) => {
      const {
        event: event2,
        scope
      } = subscriptions[0];
      return this._simulator.trigger({
        event: event2,
        scope
      });
    };
    return {
      action,
      element,
      html,
      contexts
    };
  };
  TriggerHandler.prototype._findSubscriptions = function(options) {
    return this._simulator.findSubscriptions(options);
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/features/context-pads/ContextPads.js
  var LOW_PRIORITY = 500;
  var OFFSET_TOP = -15;
  var OFFSET_LEFT = -15;
  function ContextPads(eventBus, elementRegistry, overlays, injector, canvas, scopeFilter) {
    this._elementRegistry = elementRegistry;
    this._overlays = overlays;
    this._injector = injector;
    this._canvas = canvas;
    this._scopeFilter = scopeFilter;
    this._active = false;
    this._overlayCache = /* @__PURE__ */ new Map();
    this._handlerIdx = 0;
    this._handlers = [];
    this.registerHandler("bpmn:ExclusiveGateway", ExclusiveGatewayHandler);
    this.registerHandler("bpmn:InclusiveGateway", InclusiveGatewayHandler);
    this.registerHandler("bpmn:Activity", PauseHandler);
    this.registerHandler("bpmn:Event", TriggerHandler);
    this.registerHandler("bpmn:Gateway", TriggerHandler);
    this.registerHandler("bpmn:Activity", TriggerHandler);
    eventBus.on(TOGGLE_MODE_EVENT, LOW_PRIORITY, (context) => {
      this._active = context.active;
      if (this._active) {
        this.openContextPads();
      } else {
        this.closeContextPads();
      }
    });
    eventBus.on(RESET_SIMULATION_EVENT, LOW_PRIORITY, () => {
      this.closeContextPads();
      this.openContextPads();
    });
    eventBus.on("root.set", LOW_PRIORITY, () => {
      if (this._active) {
        this.openContextPads();
      } else {
        this.closeContextPads();
      }
    });
    eventBus.on(SCOPE_FILTER_CHANGED_EVENT, (event2) => {
      const showElements = all(
        ".djs-overlay-bts-context-menu [data-scope-ids]",
        overlays._overlayRoot
      );
      for (const element of showElements) {
        const scopeIds = element.dataset.scopeIds.split(",");
        const shown = scopeIds.some((id) => scopeFilter.isShown(id));
        classes(element).toggle("hidden", !shown);
      }
      const hideElements = all(
        ".djs-overlay-bts-context-menu [data-hide-scope-ids]",
        overlays._overlayRoot
      );
      for (const element of hideElements) {
        const scopeIds = element.dataset.hideScopeIds.split(",");
        const shown = scopeIds.some((id) => scopeFilter.isShown(id));
        classes(element).toggle("hidden", shown);
      }
    });
    eventBus.on(ELEMENT_CHANGED_EVENT, LOW_PRIORITY, (event2) => {
      const {
        element
      } = event2;
      this.updateElementContextPads(element);
    });
  }
  ContextPads.prototype.registerHandler = function(type, handlerCls) {
    const handler = this._injector.instantiate(handlerCls);
    handler.hash = String(this._handlerIdx++);
    this._handlers.push({ handler, type });
  };
  ContextPads.prototype.getHandlers = function(element) {
    return this._handlers.filter(
      ({ type }) => is(element, type)
    ).map(
      ({ handler }) => handler
    );
  };
  ContextPads.prototype.openContextPads = function(parent) {
    if (!parent) {
      parent = this._canvas.getRootElement();
    }
    this._elementRegistry.forEach((element) => {
      if (isAncestor2(parent, element) && !isPlane(element)) {
        this.updateElementContextPads(element);
      }
    });
  };
  ContextPads.prototype._getOverlays = function(hash) {
    return this._overlayCache.get(hash) || [];
  };
  ContextPads.prototype._addOverlay = function(element, options) {
    const {
      handlerHash
    } = options;
    if (!handlerHash) {
      throw new Error("<handlerHash> required");
    }
    const overlayId = this._overlays.add(element, "bts-context-menu", {
      ...options,
      position: {
        top: OFFSET_TOP,
        left: OFFSET_LEFT
      },
      show: {
        minZoom: 0.5
      }
    });
    const overlay = this._overlays.get(overlayId);
    const overlayCache = this._overlayCache;
    if (!overlayCache.has(handlerHash)) {
      overlayCache.set(handlerHash, []);
    }
    overlayCache.get(handlerHash).push(overlay);
  };
  ContextPads.prototype._removeOverlay = function(overlay) {
    const {
      id,
      handlerHash
    } = overlay;
    this._overlays.remove(id);
    const overlays = this._overlayCache.get(handlerHash) || [];
    const idx = overlays.indexOf(overlay);
    if (idx !== -1) {
      overlays.splice(idx, 1);
    }
  };
  ContextPads.prototype.updateElementContextPads = function(element) {
    for (const handler of this.getHandlers(element)) {
      this._updateElementContextPads(element, handler);
    }
  };
  ContextPads.prototype._updateElementContextPads = function(element, handler) {
    const canvas = this._canvas;
    const contextPads = (handler.createContextPads(element) || []).filter((p) => p);
    const handlerHash = `${element.id}------${handler.hash}`;
    const existingOverlays = this._getOverlays(handlerHash);
    const updatedOverlays = [];
    for (const contextPad of contextPads) {
      const {
        element: element2,
        contexts: _contexts,
        hideContexts: _hideContexts,
        action: _action,
        html: _html
      } = contextPad;
      const hash = `${contextPad.element.id}-------${_html}`;
      let existingOverlay = existingOverlays.find(
        (o) => o.hash === hash
      );
      const html = existingOverlay && existingOverlay.html || domify(_html);
      if (_contexts) {
        const contexts = _contexts();
        html.dataset.scopeIds = contexts.map((c) => c.scope.id).join(",");
        const shownScopes = contexts.filter((c) => this._scopeFilter.isShown(c.scope));
        classes(html).toggle("hidden", shownScopes.length === 0);
      }
      if (_hideContexts) {
        const contexts = _hideContexts();
        html.dataset.hideScopeIds = contexts.map((c) => c.scope.id).join(",");
        const shownScopes = contexts.filter((c) => this._scopeFilter.isShown(c.scope));
        classes(html).toggle("hidden", shownScopes.length > 0);
      }
      if (existingOverlay) {
        updatedOverlays.push(existingOverlay);
        continue;
      }
      if (_action) {
        const triggerAction = () => {
          const contexts = _contexts ? _contexts().filter((c) => this._scopeFilter.isShown(c.scope)) : null;
          _action(contexts);
        };
        event.bind(html, "click", (event2) => {
          event2.preventDefault();
          triggerAction();
          if ("focus" in canvas) {
            canvas.focus();
          }
        });
        event.bind(html, "keydown", (event2) => {
          if (!isKeyboardTrigger(event2)) {
            return;
          }
          event2.preventDefault();
          triggerAction();
        });
      }
      this._addOverlay(element2, {
        hash,
        handlerHash,
        html
      });
    }
    for (const existingOverlay of existingOverlays) {
      if (!updatedOverlays.includes(existingOverlay)) {
        this._removeOverlay(existingOverlay);
      }
    }
  };
  ContextPads.prototype.closeContextPads = function() {
    for (const overlays of this._overlayCache.values()) {
      for (const overlay of overlays) {
        this._closeOverlay(overlay);
      }
    }
    this._overlayCache.clear();
  };
  ContextPads.prototype._closeOverlay = function(overlay) {
    this._overlays.remove(overlay.id);
  };
  ContextPads.$inject = [
    "eventBus",
    "elementRegistry",
    "overlays",
    "injector",
    "canvas",
    "scopeFilter"
  ];
  function isAncestor2(ancestor, descendant) {
    do {
      if (ancestor === descendant) {
        return true;
      }
      descendant = descendant.parent;
    } while (descendant);
    return false;
  }
  function isKeyboardTrigger(event2) {
    return ["Enter", " ", "Spacebar"].includes(event2.key);
  }

  // ../../node_modules/bpmn-js-token-simulation/lib/features/context-pads/index.js
  var context_pads_default = {
    __depends__: [
      scope_filter_default
    ],
    __init__: [
      "contextPads"
    ],
    contextPads: ["type", ContextPads]
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/features/simulation-state/SimulationState.js
  function SimulationState(eventBus, simulator, elementNotifications) {
    eventBus.on(SCOPE_DESTROYED_EVENT, (event2) => {
      const {
        scope
      } = event2;
      const {
        destroyInitiator,
        element: scopeElement
      } = scope;
      if (!scope.completed || !destroyInitiator) {
        return;
      }
      const processScopes = [
        "bpmn:Process",
        "bpmn:Participant"
      ];
      if (!processScopes.includes(scopeElement.type)) {
        return;
      }
      elementNotifications.addElementNotification(destroyInitiator.element, {
        type: "success",
        icon: CheckCircleIcon(),
        text: "Finished",
        scope
      });
    });
  }
  SimulationState.$inject = [
    "eventBus",
    "simulator",
    "elementNotifications"
  ];

  // ../../node_modules/bpmn-js-token-simulation/lib/features/element-notifications/ElementNotifications.js
  var OFFSET_TOP2 = -15;
  var OFFSET_RIGHT = 15;
  function ElementNotifications(overlays, eventBus) {
    this._overlays = overlays;
    eventBus.on([
      RESET_SIMULATION_EVENT,
      SCOPE_CREATE_EVENT,
      TOGGLE_MODE_EVENT
    ], () => {
      this.clear();
    });
  }
  ElementNotifications.prototype.addElementNotification = function(element, options) {
    const position = {
      top: OFFSET_TOP2,
      right: OFFSET_RIGHT
    };
    const {
      type,
      icon,
      text,
      scope = {}
    } = options;
    const colors = scope.colors;
    const colorMarkup = colors ? `style="color: ${colors.auxiliary}; background: ${colors.primary}"` : "";
    const html = domify(`
    <div class="bts-element-notification ${type || ""}" ${colorMarkup}>
      ${icon || ""}
      <span class="bts-text">${text}</span>
    </div>
  `);
    this._overlays.add(element, "bts-element-notification", {
      position,
      html,
      show: {
        minZoom: 0.5
      }
    });
  };
  ElementNotifications.prototype.clear = function() {
    this._overlays.remove({ type: "bts-element-notification" });
  };
  ElementNotifications.prototype.removeElementNotification = function(element) {
    this._overlays.remove({ element });
  };
  ElementNotifications.$inject = ["overlays", "eventBus"];

  // ../../node_modules/bpmn-js-token-simulation/lib/features/element-notifications/index.js
  var element_notifications_default = {
    elementNotifications: ["type", ElementNotifications]
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/features/notifications/Notifications.js
  var NOTIFICATION_TIME_TO_LIVE = 2e3;
  var INFO_ICON = InfoIcon();
  function Notifications(eventBus, canvas, scopeFilter) {
    this._eventBus = eventBus;
    this._canvas = canvas;
    this._scopeFilter = scopeFilter;
    this._init();
    eventBus.on([
      TOGGLE_MODE_EVENT,
      RESET_SIMULATION_EVENT
    ], (event2) => {
      this.clear();
    });
  }
  Notifications.prototype._init = function() {
    this.container = domify('<div class="bts-notifications"></div>');
    this._canvas.getContainer().appendChild(this.container);
  };
  Notifications.prototype.showNotification = function(options) {
    const {
      text,
      type = "info",
      icon = INFO_ICON,
      scope,
      ttl = NOTIFICATION_TIME_TO_LIVE
    } = options;
    if (scope && !this._scopeFilter.isShown(scope)) {
      return;
    }
    const iconMarkup = icon.startsWith("<") ? icon : `<i class="${icon}"></i>`;
    const colors = scope && scope.colors;
    const colorMarkup = colors ? `style="color: ${colors.auxiliary}; background: ${colors.primary}"` : "";
    const notification = domify(`
    <div class="bts-notification ${type}">
      <span class="bts-icon">${iconMarkup}</span>
      <span class="bts-text" title="${text}">${text}</span>
      ${scope ? `<span class="bts-scope" ${colorMarkup}>${scope.id}</span>` : ""}
    </div>
  `);
    this.container.appendChild(notification);
    while (this.container.children.length > 5) {
      this.container.children[0].remove();
    }
    setTimeout(function() {
      notification.remove();
    }, ttl);
  };
  Notifications.prototype.clear = function() {
    while (this.container.children.length) {
      this.container.children[0].remove();
    }
  };
  Notifications.$inject = [
    "eventBus",
    "canvas",
    "scopeFilter"
  ];

  // ../../node_modules/bpmn-js-token-simulation/lib/features/notifications/index.js
  var notifications_default = {
    __depends__: [
      scope_filter_default
    ],
    notifications: ["type", Notifications]
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/features/simulation-state/index.js
  var simulation_state_default = {
    __depends__: [
      element_notifications_default,
      notifications_default
    ],
    __init__: [
      "simulationState"
    ],
    simulationState: ["type", SimulationState]
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/features/show-scopes/ShowScopes.js
  var FILL_COLOR = "--token-simulation-silver-base-97";
  var STROKE_COLOR = "--token-simulation-green-base-44";
  var ID = "show-scopes";
  var VERY_HIGH_PRIORITY = 3e3;
  function ShowScopes(eventBus, canvas, scopeFilter, elementColors, simulationStyles) {
    this._eventBus = eventBus;
    this._canvas = canvas;
    this._scopeFilter = scopeFilter;
    this._elementColors = elementColors;
    this._simulationStyles = simulationStyles;
    this._highlight = null;
    this._init();
    eventBus.on(TOGGLE_MODE_EVENT, (event2) => {
      const active = event2.active;
      if (active) {
        classes(this._container).remove("hidden");
      } else {
        classes(this._container).add("hidden");
        clear(this._container);
        this.unhighlightScope();
      }
    });
    eventBus.on(SCOPE_FILTER_CHANGED_EVENT, (event2) => {
      const allElements = this.getScopeElements();
      for (const element of allElements) {
        const scopeId = element.dataset.scopeId;
        classes(element).toggle("inactive", !this._scopeFilter.isShown(scopeId));
        classes(element).toggle("focussed", this._scopeFilter.isFocused(scopeId));
        element.setAttribute("aria-pressed", String(this._scopeFilter.isFocused(scopeId)));
      }
    });
    eventBus.on(SCOPE_CREATE_EVENT, (event2) => {
      this.addScope(event2.scope);
    });
    eventBus.on(SCOPE_DESTROYED_EVENT, (event2) => {
      this.removeScope(event2.scope);
    });
    eventBus.on(SCOPE_CHANGED_EVENT, (event2) => {
      this.updateScope(event2.scope);
    });
    eventBus.on(RESET_SIMULATION_EVENT, () => {
      this.removeAllInstances();
    });
  }
  ShowScopes.prototype._init = function() {
    this._container = domify('<div class="bts-scopes hidden"></div>');
    this._canvas.getContainer().appendChild(this._container);
  };
  ShowScopes.prototype.addScope = function(scope) {
    const processElements = [
      "bpmn:Process",
      "bpmn:SubProcess",
      "bpmn:Participant"
    ];
    const {
      element: scopeElement
    } = scope;
    if (!isAny(scopeElement, processElements)) {
      return;
    }
    const colors = scope.colors;
    const colorMarkup = colors ? `style="color: ${colors.auxiliary}; background: ${colors.primary}; --scope-color: ${colors.primary}"` : "";
    const html = domify(`
    <button data-scope-id="${scope.id}" class="bts-scope"
         aria-pressed="false"
         title="Focus process instance ${scope.id}" ${colorMarkup}>
      ${scope.getTokens()}
    </button>
  `);
    event.bind(html, "click", () => {
      this._scopeFilter.toggle(scope);
    });
    event.bind(html, "mouseenter", () => {
      this.highlightScope(scopeElement);
    });
    event.bind(html, "mouseleave", () => {
      this.unhighlightScope();
    });
    if (!this._scopeFilter.isShown(scope)) {
      classes(html).add("inactive");
    }
    classes(html).toggle("focussed", this._scopeFilter.isFocused(scope));
    html.setAttribute("aria-pressed", String(this._scopeFilter.isFocused(scope)));
    this._container.appendChild(html);
  };
  ShowScopes.prototype.getScopeElements = function() {
    return all("[data-scope-id]", this._container);
  };
  ShowScopes.prototype.getScopeElement = function(scope) {
    return query(`[data-scope-id="${scope.id}"]`, this._container);
  };
  ShowScopes.prototype.updateScope = function(scope) {
    const element = this.getScopeElement(scope);
    if (element) {
      element.textContent = scope.getTokens();
    }
  };
  ShowScopes.prototype.removeScope = function(scope) {
    const element = this.getScopeElement(scope);
    if (element) {
      element.remove();
    }
  };
  ShowScopes.prototype.removeAllInstances = function() {
    this._container.innerHTML = "";
  };
  ShowScopes.prototype.highlightScope = function(element) {
    this.unhighlightScope();
    this._highlight = element;
    this._elementColors.add(element, ID, this._getHighlightColors(), VERY_HIGH_PRIORITY);
    if (!element.parent) {
      classes(this._canvas.getContainer()).add("highlight");
    }
  };
  ShowScopes.prototype.unhighlightScope = function() {
    if (!this._highlight) {
      return;
    }
    const element = this._highlight;
    this._elementColors.remove(element, ID);
    if (!element.parent) {
      classes(this._canvas.getContainer()).remove("highlight");
    }
    this._highlight = null;
  };
  ShowScopes.prototype._getHighlightColors = function() {
    return {
      fill: this._simulationStyles.get(FILL_COLOR),
      stroke: this._simulationStyles.get(STROKE_COLOR)
    };
  };
  ShowScopes.$inject = [
    "eventBus",
    "canvas",
    "scopeFilter",
    "elementColors",
    "simulationStyles"
  ];

  // ../../node_modules/bpmn-js-token-simulation/lib/features/simulation-styles/SimulationStyles.js
  function SimulationStyles() {
    this._cache = {};
  }
  SimulationStyles.$inject = [];
  SimulationStyles.prototype.get = function(prop) {
    const cachedValue = this._cache[prop];
    if (cachedValue) {
      return cachedValue;
    }
    if (!this._computedStyle) {
      this._computedStyle = this._getComputedStyle();
    }
    return this._cache[prop] = this._computedStyle.getPropertyValue(prop).trim();
  };
  SimulationStyles.prototype._getComputedStyle = function() {
    const get = typeof getComputedStyle === "function" ? getComputedStyle : getComputedStyleMock;
    const element = typeof document !== "undefined" ? document.documentElement : {};
    return get(element);
  };
  function getComputedStyleMock() {
    return {
      getPropertyValue() {
        return "";
      }
    };
  }

  // ../../node_modules/bpmn-js-token-simulation/lib/features/simulation-styles/index.js
  var simulation_styles_default = {
    simulationStyles: ["type", SimulationStyles]
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/features/show-scopes/index.js
  var show_scopes_default = {
    __depends__: [
      scope_filter_default,
      simulation_styles_default
    ],
    __init__: [
      "showScopes"
    ],
    showScopes: ["type", ShowScopes]
  };

  // ../../node_modules/diagram-js/lib/util/EscapeUtil.js
  var HTML_ESCAPE_MAP = {
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#39;"
  };
  function escapeHTML(str) {
    str = "" + str;
    return str && str.replace(/[&<>"']/g, function(match) {
      return HTML_ESCAPE_MAP[match];
    });
  }

  // ../../node_modules/bpmn-js-token-simulation/lib/features/log/Log.js
  var ICON_INFO = InfoIcon();
  function getElementName(element) {
    const name = element && element.businessObject.name;
    return name && escapeHTML(name);
  }
  function getIconForIntermediateEvent(element, throwOrCatch) {
    const eventTypeString = getEventTypeString(element);
    if (eventTypeString === "none") {
      return "bpmn-icon-intermediate-event-none";
    }
    return `bpmn-icon-intermediate-event-${throwOrCatch}-${eventTypeString}`;
  }
  function getEventTypeString(element) {
    const bo = getBusinessObject(element);
    if (bo.get("eventDefinitions").length === 0) {
      return "none";
    }
    const eventDefinition = bo.eventDefinitions[0];
    if (is(eventDefinition, "bpmn:MessageEventDefinition")) {
      return "message";
    }
    if (is(eventDefinition, "bpmn:TimerEventDefinition")) {
      return "timer";
    }
    if (is(eventDefinition, "bpmn:SignalEventDefinition")) {
      return "signal";
    }
    if (is(eventDefinition, "bpmn:ErrorEventDefinition")) {
      return "error";
    }
    if (is(eventDefinition, "bpmn:EscalationEventDefinition")) {
      return "escalation";
    }
    if (is(eventDefinition, "bpmn:CompensateEventDefinition")) {
      return "compensation";
    }
    if (is(eventDefinition, "bpmn:ConditionalEventDefinition")) {
      return "condition";
    }
    if (is(eventDefinition, "bpmn:LinkEventDefinition")) {
      return "link";
    }
    if (is(eventDefinition, "bpmn:CancelEventDefinition")) {
      return "cancel";
    }
    if (is(eventDefinition, "bpmn:TerminateEventDefinition")) {
      return "terminate";
    }
    return "none";
  }
  function Log(eventBus, notifications, tokenSimulationPalette, canvas, scopeFilter, simulator) {
    this._notifications = notifications;
    this._tokenSimulationPalette = tokenSimulationPalette;
    this._canvas = canvas;
    this._scopeFilter = scopeFilter;
    this._init();
    eventBus.on(SCOPE_FILTER_CHANGED_EVENT, (event2) => {
      const allElements = all(".bts-entry[data-scope-id]", this._container);
      for (const element of allElements) {
        const scopeId = element.dataset.scopeId;
        classes(element).toggle("inactive", !this._scopeFilter.isShown(scopeId));
      }
    });
    eventBus.on(SCOPE_DESTROYED_EVENT, (event2) => {
      const {
        scope
      } = event2;
      const {
        element: scopeElement
      } = scope;
      const completed = scope.completed;
      const processScopes = [
        "bpmn:Process",
        "bpmn:Participant",
        "bpmn:SubProcess"
      ];
      if (!isAny(scopeElement, processScopes)) {
        return;
      }
      const isSubProcess = is(scopeElement, "bpmn:SubProcess");
      const text = `${isSubProcess ? getElementName(scopeElement) || "SubProcess" : "Process"} ${completed ? "finished" : "canceled"}`;
      this.log({
        text,
        icon: completed ? CheckCircleIcon() : TimesCircleIcon(),
        scope
      });
    });
    eventBus.on(SCOPE_CREATE_EVENT, (event2) => {
      const {
        scope
      } = event2;
      const {
        element: scopeElement
      } = scope;
      const processScopes = [
        "bpmn:Process",
        "bpmn:Participant",
        "bpmn:SubProcess"
      ];
      if (!isAny(scopeElement, processScopes)) {
        return;
      }
      const isSubProcess = is(scopeElement, "bpmn:SubProcess");
      const text = `${isSubProcess ? getElementName(scopeElement) || "SubProcess" : "Process"} started`;
      this.log({
        text,
        icon: CheckCircleIcon(),
        scope
      });
    });
    eventBus.on(TRACE_EVENT, (event2) => {
      const {
        action,
        scope: elementScope,
        element
      } = event2;
      if (action !== "exit") {
        return;
      }
      const scope = elementScope.parent;
      const elementName = getElementName(element);
      if (is(element, "bpmn:ServiceTask")) {
        return this.log({
          text: elementName || "Service Task",
          icon: "bpmn-icon-service",
          scope
        });
      }
      if (is(element, "bpmn:UserTask")) {
        return this.log({
          text: elementName || "User Task",
          icon: "bpmn-icon-user",
          scope
        });
      }
      if (is(element, "bpmn:CallActivity")) {
        return this.log({
          text: elementName || "Call Activity",
          icon: "bpmn-icon-call-activity",
          scope
        });
      }
      if (is(element, "bpmn:ScriptTask")) {
        return this.log({
          text: elementName || "Script Task",
          icon: "bpmn-icon-script",
          scope
        });
      }
      if (is(element, "bpmn:BusinessRuleTask")) {
        return this.log({
          text: elementName || "Business Rule Task",
          icon: "bpmn-icon-business-rule",
          scope
        });
      }
      if (is(element, "bpmn:ManualTask")) {
        return this.log({
          text: elementName || "Manual Task",
          icon: "bpmn-icon-manual-task",
          scope
        });
      }
      if (is(element, "bpmn:ReceiveTask")) {
        return this.log({
          text: elementName || "Receive Task",
          icon: "bpmn-icon-receive",
          scope
        });
      }
      if (is(element, "bpmn:SendTask")) {
        return this.log({
          text: elementName || "Send Task",
          icon: "bpmn-icon-send",
          scope
        });
      }
      if (is(element, "bpmn:Task")) {
        return this.log({
          text: elementName || "Task",
          icon: "bpmn-icon-task",
          scope
        });
      }
      if (is(element, "bpmn:ExclusiveGateway")) {
        return this.log({
          text: elementName || "Exclusive Gateway",
          icon: "bpmn-icon-gateway-xor",
          scope
        });
      }
      if (is(element, "bpmn:ParallelGateway")) {
        return this.log({
          text: elementName || "Parallel Gateway",
          icon: "bpmn-icon-gateway-parallel",
          scope
        });
      }
      if (is(element, "bpmn:InclusiveGateway")) {
        return this.log({
          text: elementName || "Inclusive Gateway",
          icon: "bpmn-icon-gateway-or",
          scope
        });
      }
      if (is(element, "bpmn:StartEvent")) {
        return this.log({
          text: elementName || "Start Event",
          icon: `bpmn-icon-start-event-${getEventTypeString(element)}`,
          scope
        });
      }
      if (is(element, "bpmn:IntermediateCatchEvent")) {
        return this.log({
          text: elementName || "Intermediate Event",
          icon: getIconForIntermediateEvent(element, "catch"),
          scope
        });
      }
      if (is(element, "bpmn:IntermediateThrowEvent")) {
        return this.log({
          text: elementName || "Intermediate Event",
          icon: getIconForIntermediateEvent(element, "throw"),
          scope
        });
      }
      if (is(element, "bpmn:BoundaryEvent")) {
        return this.log({
          text: elementName || "Boundary Event",
          icon: getIconForIntermediateEvent(element, "catch"),
          scope
        });
      }
      if (is(element, "bpmn:EndEvent")) {
        return this.log({
          text: elementName || "End Event",
          icon: `bpmn-icon-end-event-${getEventTypeString(element)}`,
          scope
        });
      }
    });
    eventBus.on([
      TOGGLE_MODE_EVENT,
      RESET_SIMULATION_EVENT
    ], (event2) => {
      this.clear();
      this.toggle(false);
    });
  }
  Log.prototype._init = function() {
    this._container = domify(`
    <div class="bts-log hidden djs-scrollable">
      <div class="bts-header">
        ${LogIcon("bts-log-icon")}
        Simulation Log
        <button class="bts-close" aria-label="Close">
          ${TimesIcon()}
        </button>
      </div>
      <div class="bts-content">
        <p class="bts-entry placeholder">No Entries</p>
      </div>
    </div>
  `);
    this._placeholder = query(".bts-placeholder", this._container);
    this._content = query(".bts-content", this._container);
    event.bind(this._content, "mousedown", (event2) => {
      event2.stopPropagation();
    });
    this._close = query(".bts-close", this._container);
    event.bind(this._close, "click", () => {
      this.toggle(false);
    });
    this._icon = query(".bts-log-icon", this._container);
    event.bind(this._icon, "click", () => {
      this.toggle();
    });
    this._canvas.getContainer().appendChild(this._container);
    this.paletteEntry = domify(`
    <button class="bts-entry" title="Toggle Simulation Log">
      ${LogIcon()}
    </button>
  `);
    event.bind(this.paletteEntry, "click", () => {
      this.toggle();
    });
    this._tokenSimulationPalette.addEntry(this.paletteEntry, 3);
  };
  Log.prototype.isShown = function() {
    const container = this._container;
    return !classes(container).has("hidden");
  };
  Log.prototype.toggle = function(shown = !this.isShown()) {
    const container = this._container;
    if (shown) {
      classes(container).remove("hidden");
    } else {
      classes(container).add("hidden");
    }
  };
  Log.prototype.log = function(options) {
    const {
      text,
      type = "info",
      icon = ICON_INFO,
      scope
    } = options;
    const content = this._content;
    classes(this._placeholder).add("hidden");
    if (!this.isShown()) {
      this._notifications.showNotification(options);
    }
    const iconMarkup = icon.startsWith("<") ? icon : `<i class="${icon}"></i>`;
    const colors = scope && scope.colors;
    const colorMarkup = colors ? `style="background: ${colors.primary}; color: ${colors.auxiliary}"` : "";
    const logEntry = domify(`
    <p class="bts-entry ${type} ${scope && this._scopeFilter.isShown(scope) ? "" : "inactive"}" ${scope ? `data-scope-id="${scope.id}"` : ""}>
      <span class="bts-icon">${iconMarkup}</span>
      <span class="bts-text" title="${text}">${text}</span>
      ${scope ? `<span class="bts-scope" data-scope-id="${scope.id}" ${colorMarkup}>${scope.id}</span>` : ""}
    </p>
  `);
    delegate.bind(logEntry, ".bts-scope[data-scope-id]", "click", (event2) => {
      this._scopeFilter.toggle(scope);
    });
    const shouldScroll = Math.abs(content.clientHeight + content.scrollTop - content.scrollHeight) < 2;
    content.appendChild(logEntry);
    if (shouldScroll) {
      content.scrollTop = content.scrollHeight;
    }
  };
  Log.prototype.clear = function() {
    while (this._content.firstChild) {
      this._content.removeChild(this._content.firstChild);
    }
    this._placeholder = domify('<p class="bts-entry placeholder">No Entries</p>');
    this._content.appendChild(this._placeholder);
  };
  Log.$inject = [
    "eventBus",
    "notifications",
    "tokenSimulationPalette",
    "canvas",
    "scopeFilter",
    "simulator"
  ];

  // ../../node_modules/bpmn-js-token-simulation/lib/features/log/index.js
  var log_default = {
    __depends__: [
      notifications_default,
      scope_filter_default
    ],
    __init__: [
      "log"
    ],
    log: ["type", Log]
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/features/element-support/ElementSupport.js
  var UNSUPPORTED_ELEMENTS = [
    "bpmn:ComplexGateway"
  ];
  function isLabel2(element) {
    return element.labelTarget;
  }
  function ElementSupport(eventBus, elementRegistry, canvas, notifications, elementNotifications) {
    this._eventBus = eventBus;
    this._elementRegistry = elementRegistry;
    this._elementNotifications = elementNotifications;
    this._notifications = notifications;
    this._canvasParent = canvas.getContainer().parentNode;
    eventBus.on(TOGGLE_MODE_EVENT, (event2) => {
      if (event2.active) {
        this.enable();
      } else {
        this.clear();
      }
    });
  }
  ElementSupport.prototype.getUnsupportedElements = function() {
    return this._unsupportedElements;
  };
  ElementSupport.prototype.enable = function() {
    const unsupportedElements = [];
    this._elementRegistry.forEach((element) => {
      if (isLabel2(element)) {
        return;
      }
      if (!isAny(element, UNSUPPORTED_ELEMENTS)) {
        return;
      }
      this.showWarning(element);
      unsupportedElements.push(element);
    });
    if (unsupportedElements.length) {
      this._notifications.showNotification({
        text: "Found unsupported elements",
        icon: ExclamationTriangleIcon(),
        type: "warning",
        ttl: 5e3
      });
    }
    this._unsupportedElements = unsupportedElements;
  };
  ElementSupport.prototype.clear = function() {
    classes(this._canvasParent).remove("warning");
  };
  ElementSupport.prototype.showWarning = function(element) {
    this._elementNotifications.addElementNotification(element, {
      type: "warning",
      icon: ExclamationTriangleIcon(),
      text: "Not supported"
    });
  };
  ElementSupport.$inject = [
    "eventBus",
    "elementRegistry",
    "canvas",
    "notifications",
    "elementNotifications"
  ];

  // ../../node_modules/bpmn-js-token-simulation/lib/features/element-support/index.js
  var element_support_default = {
    __depends__: [
      element_notifications_default,
      notifications_default
    ],
    __init__: ["elementSupport"],
    elementSupport: ["type", ElementSupport]
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/features/pause-simulation/PauseSimulation.js
  var PLAY_MARKUP = PlayIcon();
  var PAUSE_MARKUP = PauseIcon();
  var HIGH_PRIORITY3 = 1500;
  function PauseSimulation(eventBus, tokenSimulationPalette, notifications, canvas) {
    this._eventBus = eventBus;
    this._tokenSimulationPalette = tokenSimulationPalette;
    this._notifications = notifications;
    this.canvasParent = canvas.getContainer().parentNode;
    this.isActive = false;
    this.isPaused = true;
    this._init();
    eventBus.on(SCOPE_CREATE_EVENT, HIGH_PRIORITY3, (event2) => {
      this.activate();
      this.unpause();
    });
    eventBus.on([
      RESET_SIMULATION_EVENT,
      TOGGLE_MODE_EVENT
    ], () => {
      this.deactivate();
      this.pause();
    });
    eventBus.on(TRACE_EVENT, HIGH_PRIORITY3, (event2) => {
      this.unpause();
    });
  }
  PauseSimulation.prototype._init = function() {
    this.paletteEntry = domify(`
    <button class="bts-entry disabled" title="Play/Pause Simulation" disabled>
      ${PLAY_MARKUP}
    </button>
  `);
    event.bind(this.paletteEntry, "click", this.toggle.bind(this));
    this._tokenSimulationPalette.addEntry(this.paletteEntry, 1);
  };
  PauseSimulation.prototype.toggle = function() {
    if (this.isPaused) {
      this.unpause();
    } else {
      this.pause();
    }
  };
  PauseSimulation.prototype.pause = function() {
    if (!this.isActive) {
      return;
    }
    classes(this.paletteEntry).remove("active");
    classes(this.canvasParent).add("paused");
    this.paletteEntry.innerHTML = PLAY_MARKUP;
    this._eventBus.fire(PAUSE_SIMULATION_EVENT);
    this._notifications.showNotification({
      text: "Pause Simulation"
    });
    this.isPaused = true;
  };
  PauseSimulation.prototype.unpause = function() {
    if (!this.isActive || !this.isPaused) {
      return;
    }
    classes(this.paletteEntry).add("active");
    classes(this.canvasParent).remove("paused");
    this.paletteEntry.innerHTML = PAUSE_MARKUP;
    this._eventBus.fire(PLAY_SIMULATION_EVENT);
    this._notifications.showNotification({
      text: "Play Simulation"
    });
    this.isPaused = false;
  };
  PauseSimulation.prototype.activate = function() {
    this.isActive = true;
    classes(this.paletteEntry).remove("disabled");
    this.paletteEntry.removeAttribute("disabled");
  };
  PauseSimulation.prototype.deactivate = function() {
    this.isActive = false;
    classes(this.paletteEntry).remove("active");
    classes(this.paletteEntry).add("disabled");
    this.paletteEntry.setAttribute("disabled", "");
  };
  PauseSimulation.$inject = [
    "eventBus",
    "tokenSimulationPalette",
    "notifications",
    "canvas"
  ];

  // ../../node_modules/bpmn-js-token-simulation/lib/features/pause-simulation/index.js
  var pause_simulation_default = {
    __depends__: [
      notifications_default
    ],
    __init__: [
      "pauseSimulation"
    ],
    pauseSimulation: ["type", PauseSimulation]
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/features/reset-simulation/ResetSimulation.js
  function ResetSimulation(eventBus, tokenSimulationPalette, notifications) {
    this._eventBus = eventBus;
    this._tokenSimulationPalette = tokenSimulationPalette;
    this._notifications = notifications;
    this._init();
    eventBus.on(SCOPE_CREATE_EVENT, () => {
      classes(this._paletteEntry).remove("disabled");
      this._paletteEntry.removeAttribute("disabled");
    });
    eventBus.on(TOGGLE_MODE_EVENT, (event2) => {
      const active = this._active = event2.active;
      if (!active) {
        this.resetSimulation();
      }
    });
  }
  ResetSimulation.prototype._init = function() {
    this._paletteEntry = domify(`
    <button class="bts-entry disabled" title="Reset Simulation" disabled>
      ${ResetIcon()}
    </button>
  `);
    event.bind(this._paletteEntry, "click", () => {
      this.resetSimulation();
      this._notifications.showNotification({
        text: "Reset Simulation",
        type: "info"
      });
    });
    this._tokenSimulationPalette.addEntry(this._paletteEntry, 2);
  };
  ResetSimulation.prototype.resetSimulation = function() {
    classes(this._paletteEntry).add("disabled");
    this._paletteEntry.setAttribute("disabled", "");
    this._eventBus.fire(RESET_SIMULATION_EVENT);
  };
  ResetSimulation.$inject = [
    "eventBus",
    "tokenSimulationPalette",
    "notifications"
  ];

  // ../../node_modules/bpmn-js-token-simulation/lib/features/reset-simulation/index.js
  var reset_simulation_default = {
    __depends__: [
      notifications_default
    ],
    __init__: [
      "resetSimulation"
    ],
    resetSimulation: ["type", ResetSimulation]
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/features/token-count/TokenCount.js
  var OFFSET_BOTTOM = 10;
  var OFFSET_LEFT2 = -15;
  var LOW_PRIORITY2 = 500;
  var DEFAULT_PRIMARY_COLOR2 = "--token-simulation-green-base-44";
  var DEFAULT_AUXILIARY_COLOR2 = "--token-simulation-white";
  function TokenCount(eventBus, overlays, simulator, scopeFilter, simulationStyles) {
    this._overlays = overlays;
    this._scopeFilter = scopeFilter;
    this._simulator = simulator;
    this._simulationStyles = simulationStyles;
    this.overlayIds = {};
    eventBus.on(ELEMENT_CHANGED_EVENT, LOW_PRIORITY2, (event2) => {
      const {
        element
      } = event2;
      this.removeTokenCounts(element);
      this.addTokenCounts(element);
    });
    eventBus.on(SCOPE_FILTER_CHANGED_EVENT, (event2) => {
      const allElements = all(".bts-token-count[data-scope-id]", overlays._overlayRoot);
      for (const element of allElements) {
        const scopeId = element.dataset.scopeId;
        classes(element).toggle("inactive", !this._scopeFilter.isShown(scopeId));
      }
    });
  }
  TokenCount.prototype.addTokenCounts = function(element) {
    if (is(element, "bpmn:MessageFlow") || is(element, "bpmn:SequenceFlow")) {
      return;
    }
    const scopes = this._simulator.findScopes((scope) => {
      return !scope.destroyed && scope.children.some((c) => !c.destroyed && c.element === element);
    });
    this.addTokenCount(element, scopes);
  };
  TokenCount.prototype.addTokenCount = function(element, scopes) {
    if (!scopes.length) {
      return;
    }
    const tokenMarkup = scopes.map((scope) => {
      return this._getTokenHTML(element, scope);
    }).join("");
    const html = domify(`
    <div class="bts-token-count-parent">
      ${tokenMarkup}
    </div>
  `);
    const position = { bottom: OFFSET_BOTTOM, left: OFFSET_LEFT2 };
    const overlayId = this._overlays.add(element, "bts-token-count", {
      position,
      html,
      show: {
        minZoom: 0.5
      }
    });
    this.overlayIds[element.id] = overlayId;
  };
  TokenCount.prototype.removeTokenCounts = function(element) {
    this.removeTokenCount(element);
  };
  TokenCount.prototype.removeTokenCount = function(element) {
    const overlayId = this.overlayIds[element.id];
    if (!overlayId) {
      return;
    }
    this._overlays.remove(overlayId);
    delete this.overlayIds[element.id];
  };
  TokenCount.prototype._getTokenHTML = function(element, scope) {
    const colors = scope.colors || this._getDefaultColors();
    return `
    <div data-scope-id="${scope.id}" class="bts-token-count waiting ${this._scopeFilter.isShown(scope) ? "" : "inactive"}"
         style="color: ${colors.auxiliary}; background: ${colors.primary}">
      ${scope.getTokensByElement(element)}
    </div>
  `;
  };
  TokenCount.prototype._getDefaultColors = function() {
    return {
      primary: this._simulationStyles.get(DEFAULT_PRIMARY_COLOR2),
      auxiliary: this._simuationStyles.get(DEFAULT_AUXILIARY_COLOR2)
    };
  };
  TokenCount.$inject = [
    "eventBus",
    "overlays",
    "simulator",
    "scopeFilter",
    "simulationStyles"
  ];

  // ../../node_modules/bpmn-js-token-simulation/lib/features/token-count/index.js
  var token_count_default = {
    __depends__: [
      scope_filter_default,
      simulation_styles_default
    ],
    __init__: [
      "tokenCount"
    ],
    tokenCount: ["type", TokenCount]
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/features/set-animation-speed/SetAnimationSpeed.js
  var SPEEDS = [
    ["Slow", 0.5],
    ["Normal", 1],
    ["Fast", 2]
  ];
  function SetAnimationSpeed(canvas, animation, eventBus) {
    this._canvas = canvas;
    this._animation = animation;
    this._eventBus = eventBus;
    this._init(animation.getAnimationSpeed());
    eventBus.on(TOGGLE_MODE_EVENT, (event2) => {
      const active = event2.active;
      if (!active) {
        classes(this._container).add("hidden");
      } else {
        classes(this._container).remove("hidden");
      }
    });
    eventBus.on(ANIMATION_SPEED_CHANGED_EVENT, (event2) => {
      this.setActive(event2.speed);
    });
  }
  SetAnimationSpeed.prototype.getToggleSpeed = function(element) {
    return parseFloat(element.dataset.speed);
  };
  SetAnimationSpeed.prototype._init = function(animationSpeed) {
    this._container = domify(`
    <div class="bts-set-animation-speed hidden">
      ${TachometerIcon()}
      <div class="bts-animation-speed-buttons">
        ${SPEEDS.map(([label, speed], idx) => `
            <button title="Set animation speed = ${label}" data-speed="${speed}" class="bts-animation-speed-button ${speed === animationSpeed ? "active" : ""}">
              ${Array.from({ length: idx + 1 }).map(
      () => AngleRightIcon()
    ).join("")}
            </button>
          `).join("")}
      </div>
    </div>
  `);
    delegate.bind(this._container, "[data-speed]", "click", (event2) => {
      const toggle = event2.delegateTarget;
      const speed = this.getToggleSpeed(toggle);
      this._animation.setAnimationSpeed(speed);
    });
    this._canvas.getContainer().appendChild(this._container);
  };
  SetAnimationSpeed.prototype.setActive = function(speed) {
    all("[data-speed]", this._container).forEach((toggle) => {
      const active = this.getToggleSpeed(toggle) === speed;
      classes(toggle)[active ? "add" : "remove"]("active");
    });
  };
  SetAnimationSpeed.$inject = [
    "canvas",
    "animation",
    "eventBus"
  ];

  // ../../node_modules/bpmn-js-token-simulation/lib/features/set-animation-speed/index.js
  var set_animation_speed_default = {
    __init__: [
      "setAnimationSpeed"
    ],
    setAnimationSpeed: ["type", SetAnimationSpeed]
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/features/exclusive-gateway-settings/ExclusiveGatewaySettings.js
  var SELECTED_COLOR = "--token-simulation-grey-darken-30";
  var NOT_SELECTED_COLOR = "--token-simulation-grey-lighten-56";
  function getNext(gateway, sequenceFlow) {
    var outgoing = gateway.outgoing.filter(isSequenceFlow2);
    var index2 = outgoing.indexOf(sequenceFlow || gateway.sequenceFlow);
    if (outgoing[index2 + 1]) {
      return outgoing[index2 + 1];
    } else {
      return outgoing[0];
    }
  }
  function isSequenceFlow2(connection) {
    return is(connection, "bpmn:SequenceFlow");
  }
  var ID2 = "exclusive-gateway-settings";
  var HIGH_PRIORITY4 = 2e3;
  function ExclusiveGatewaySettings(eventBus, elementRegistry, elementColors, simulator, simulationStyles) {
    this._elementRegistry = elementRegistry;
    this._elementColors = elementColors;
    this._simulator = simulator;
    this._simulationStyles = simulationStyles;
    eventBus.on(TOGGLE_MODE_EVENT, (event2) => {
      if (event2.active) {
        this.setSequenceFlowsDefault();
      } else {
        this.resetSequenceFlows();
      }
    });
  }
  ExclusiveGatewaySettings.prototype.setSequenceFlowsDefault = function() {
    const exclusiveGateways = this._elementRegistry.filter((element) => {
      return is(element, "bpmn:ExclusiveGateway");
    });
    for (const gateway of exclusiveGateways) {
      this.setSequenceFlow(gateway);
    }
  };
  ExclusiveGatewaySettings.prototype.resetSequenceFlows = function() {
    const exclusiveGateways = this._elementRegistry.filter((element) => {
      return is(element, "bpmn:ExclusiveGateway");
    });
    exclusiveGateways.forEach((exclusiveGateway) => {
      if (exclusiveGateway.outgoing.filter(isSequenceFlow2).length) {
        this.resetSequenceFlow(exclusiveGateway);
      }
    });
  };
  ExclusiveGatewaySettings.prototype.resetSequenceFlow = function(gateway) {
    this._simulator.setConfig(gateway, { activeOutgoing: void 0 });
  };
  ExclusiveGatewaySettings.prototype.setSequenceFlow = function(gateway) {
    const outgoing = gateway.outgoing.filter(isSequenceFlow2);
    if (outgoing.length < 2) {
      return;
    }
    const {
      activeOutgoing
    } = this._simulator.getConfig(gateway);
    let newActiveOutgoing;
    if (activeOutgoing) {
      newActiveOutgoing = getNext(gateway, activeOutgoing);
    } else {
      newActiveOutgoing = outgoing[0];
    }
    this._simulator.setConfig(gateway, { activeOutgoing: newActiveOutgoing });
    gateway.outgoing.forEach((outgoing2) => {
      const style = outgoing2 === newActiveOutgoing ? SELECTED_COLOR : NOT_SELECTED_COLOR;
      const stroke = this._simulationStyles.get(style);
      this._elementColors.add(outgoing2, ID2, {
        stroke
      }, HIGH_PRIORITY4);
    });
  };
  ExclusiveGatewaySettings.$inject = [
    "eventBus",
    "elementRegistry",
    "elementColors",
    "simulator",
    "simulationStyles"
  ];

  // ../../node_modules/bpmn-js-token-simulation/lib/features/element-colors/ElementColors.js
  var VERY_HIGH_PRIORITY2 = 5e4;
  function ElementColors(elementRegistry, eventBus, graphicsFactory) {
    this._elementRegistry = elementRegistry;
    this._eventBus = eventBus;
    this._graphicsFactory = graphicsFactory;
    this._originalColors = {};
    this._customColors = {};
    eventBus.on(TOGGLE_MODE_EVENT, VERY_HIGH_PRIORITY2, (event2) => {
      const active = event2.active;
      if (active) {
        this._saveOriginalColors();
      } else {
        this._applyOriginalColors();
        this._originalColors = {};
        this._customColors = {};
      }
    });
    eventBus.on("saveXML.start", VERY_HIGH_PRIORITY2, () => {
      this._applyOriginalColors();
      eventBus.once("saveXML.done", () => this._applyCustomColors());
    });
  }
  ElementColors.$inject = [
    "elementRegistry",
    "eventBus",
    "graphicsFactory"
  ];
  ElementColors.prototype.add = function(element, id, colors, priority = 1e3) {
    let elementColors = this._customColors[element.id];
    if (!elementColors) {
      elementColors = this._customColors[element.id] = {};
    }
    elementColors[id] = {
      ...colors,
      priority
    };
    this._applyHighestPriorityColor(element);
  };
  ElementColors.prototype.remove = function(element, id) {
    const elementColors = this._customColors[element.id];
    if (elementColors) {
      delete elementColors[id];
      if (!Object.keys(elementColors)) {
        delete this._customColors[element.id];
      }
    }
    this._applyHighestPriorityColor(element);
  };
  ElementColors.prototype._get = function(element) {
    const di = getDi(element);
    if (!di) {
      return void 0;
    }
    if (isLabel3(element)) {
      return {
        stroke: di.label && di.label.get("color")
      };
    } else if (isAny(di, ["bpmndi:BPMNEdge", "bpmndi:BPMNShape"])) {
      return {
        fill: di.get("background-color"),
        stroke: di.get("border-color")
      };
    }
  };
  ElementColors.prototype._set = function(element, colors = {}) {
    const {
      fill,
      stroke
    } = colors;
    const di = getDi(element);
    if (!di) {
      return;
    }
    if (isLabel3(element)) {
      di.label && di.label.set("color", stroke);
    } else if (isAny(di, ["bpmndi:BPMNEdge", "bpmndi:BPMNShape"])) {
      di.set("background-color", fill);
      di.set("border-color", stroke);
    }
    this._forceRedraw(element);
  };
  ElementColors.prototype._saveOriginalColors = function() {
    this._originalColors = {};
    this._elementRegistry.forEach((element) => {
      this._originalColors[element.id] = this._get(element);
    });
  };
  ElementColors.prototype._applyOriginalColors = function() {
    this._elementRegistry.forEach((element) => {
      const colors = this._originalColors[element.id];
      if (colors) {
        this._set(element, colors);
      }
    });
  };
  ElementColors.prototype._applyCustomColors = function() {
    this._elementRegistry.forEach((element) => {
      const elementColors = this._customColors[element.id];
      if (elementColors) {
        this._set(element, getColorsWithHighestPriority(elementColors));
      }
    });
  };
  ElementColors.prototype._applyHighestPriorityColor = function(element) {
    const elementColors = this._customColors[element.id];
    if (!elementColors) {
      this._set(element, this._originalColors[element.id]);
      return;
    }
    this._set(element, getColorsWithHighestPriority(elementColors));
  };
  ElementColors.prototype._forceRedraw = function(element) {
    const gfx = this._elementRegistry.getGraphics(element);
    const type = element.waypoints ? "connection" : "shape";
    this._graphicsFactory.update(type, element, gfx);
  };
  function isLabel3(element) {
    return "labelTarget" in element;
  }
  function getColorsWithHighestPriority(colors = {}) {
    const colorsWithHighestPriority = Object.values(colors).reduce((colorsWithHighestPriority2, colors2) => {
      const { priority = 1e3 } = colors2;
      if (!colorsWithHighestPriority2 || priority > colorsWithHighestPriority2.priority) {
        return colors2;
      }
      return colorsWithHighestPriority2;
    }, void 0);
    if (colorsWithHighestPriority) {
      const { priority, ...fillAndStroke } = colorsWithHighestPriority;
      return fillAndStroke;
    }
  }

  // ../../node_modules/bpmn-js-token-simulation/lib/features/element-colors/index.js
  var element_colors_default = {
    elementColors: ["type", ElementColors]
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/features/exclusive-gateway-settings/index.js
  var exclusive_gateway_settings_default = {
    __depends__: [
      element_colors_default,
      simulation_styles_default
    ],
    exclusiveGatewaySettings: ["type", ExclusiveGatewaySettings]
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/features/neutral-element-colors/NeutralElementColors.js
  var ID3 = "neutral-element-colors";
  function NeutralElementColors(eventBus, elementRegistry, elementColors) {
    this._elementRegistry = elementRegistry;
    this._elementColors = elementColors;
    eventBus.on(TOGGLE_MODE_EVENT, (event2) => {
      const { active } = event2;
      if (active) {
        this._setNeutralColors();
      }
    });
  }
  NeutralElementColors.prototype._setNeutralColors = function() {
    this._elementRegistry.forEach((element) => {
      this._elementColors.add(element, ID3, {
        stroke: "#212121",
        fill: "#fff"
      });
    });
  };
  NeutralElementColors.$inject = [
    "eventBus",
    "elementRegistry",
    "elementColors"
  ];

  // ../../node_modules/bpmn-js-token-simulation/lib/features/neutral-element-colors/index.js
  var neutral_element_colors_default = {
    __depends__: [element_colors_default],
    __init__: [
      "neutralElementColors"
    ],
    neutralElementColors: ["type", NeutralElementColors]
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/features/inclusive-gateway-settings/InclusiveGatewaySettings.js
  var SELECTED_COLOR2 = "--token-simulation-grey-darken-30";
  var NOT_SELECTED_COLOR2 = "--token-simulation-grey-lighten-56";
  var COLOR_ID = "inclusive-gateway-settings";
  function InclusiveGatewaySettings(eventBus, elementRegistry, elementColors, simulator, simulationStyles) {
    this._elementRegistry = elementRegistry;
    this._elementColors = elementColors;
    this._simulator = simulator;
    this._simulationStyles = simulationStyles;
    eventBus.on(TOGGLE_MODE_EVENT, (event2) => {
      if (event2.active) {
        this.setDefaults();
      } else {
        this.reset();
      }
    });
  }
  InclusiveGatewaySettings.prototype.setDefaults = function() {
    const inclusiveGateways = this._elementRegistry.filter((element) => {
      return is(element, "bpmn:InclusiveGateway");
    });
    inclusiveGateways.forEach((inclusiveGateway) => {
      if (inclusiveGateway.outgoing.filter(isSequenceFlow).length > 1) {
        this._setGatewayDefaults(inclusiveGateway);
      }
    });
  };
  InclusiveGatewaySettings.prototype.reset = function() {
    const inclusiveGateways = this._elementRegistry.filter((element) => {
      return is(element, "bpmn:InclusiveGateway");
    });
    inclusiveGateways.forEach((inclusiveGateway) => {
      if (inclusiveGateway.outgoing.filter(isSequenceFlow).length > 1) {
        this._resetGateway(inclusiveGateway);
      }
    });
  };
  InclusiveGatewaySettings.prototype.toggleSequenceFlow = function(gateway, sequenceFlow) {
    const activeOutgoing = this._getActiveOutgoing(gateway), defaultFlow = getDefaultFlow(gateway), nonDefaultFlows = getNonDefaultFlows(gateway);
    let newActiveOutgoing;
    if (activeOutgoing.includes(sequenceFlow)) {
      newActiveOutgoing = without(activeOutgoing, sequenceFlow);
    } else {
      newActiveOutgoing = without(activeOutgoing, defaultFlow).concat(sequenceFlow);
    }
    if (!newActiveOutgoing.length) {
      if (defaultFlow) {
        newActiveOutgoing = [defaultFlow];
      } else {
        newActiveOutgoing = [nonDefaultFlows.find((flow) => flow !== sequenceFlow)];
      }
    }
    this._setActiveOutgoing(gateway, newActiveOutgoing);
  };
  InclusiveGatewaySettings.prototype._getActiveOutgoing = function(gateway) {
    const {
      activeOutgoing
    } = this._simulator.getConfig(gateway);
    return activeOutgoing;
  };
  InclusiveGatewaySettings.prototype._setActiveOutgoing = function(gateway, activeOutgoing) {
    this._simulator.setConfig(gateway, { activeOutgoing });
    const sequenceFlows = gateway.outgoing.filter(isSequenceFlow);
    sequenceFlows.forEach((outgoing) => {
      const style = !activeOutgoing || activeOutgoing.includes(outgoing) ? SELECTED_COLOR2 : NOT_SELECTED_COLOR2;
      const stroke = this._simulationStyles.get(style);
      this._elementColors.add(outgoing, COLOR_ID, {
        stroke
      });
    });
  };
  InclusiveGatewaySettings.prototype._setGatewayDefaults = function(gateway) {
    const sequenceFlows = gateway.outgoing.filter(isSequenceFlow);
    const defaultFlow = getDefaultFlow(gateway);
    const nonDefaultFlows = without(sequenceFlows, defaultFlow);
    this._setActiveOutgoing(gateway, nonDefaultFlows);
  };
  InclusiveGatewaySettings.prototype._resetGateway = function(gateway) {
    this._simulator.setConfig(gateway, { activeOutgoing: void 0 });
  };
  InclusiveGatewaySettings.$inject = [
    "eventBus",
    "elementRegistry",
    "elementColors",
    "simulator",
    "simulationStyles"
  ];
  function getDefaultFlow(gateway) {
    const defaultFlow = getBusinessObject(gateway).default;
    if (!defaultFlow) {
      return;
    }
    return gateway.outgoing.find((flow) => {
      const flowBo = getBusinessObject(flow);
      return flowBo === defaultFlow;
    });
  }
  function getNonDefaultFlows(gateway) {
    const defaultFlow = getDefaultFlow(gateway);
    return gateway.outgoing.filter((flow) => {
      const flowBo = getBusinessObject(flow);
      return flowBo !== defaultFlow;
    });
  }
  function without(array, element) {
    return array.filter((arrayElement) => arrayElement !== element);
  }

  // ../../node_modules/bpmn-js-token-simulation/lib/features/inclusive-gateway-settings/index.js
  var inclusive_gateway_settings_default = {
    __depends__: [
      element_colors_default,
      simulation_styles_default
    ],
    inclusiveGatewaySettings: ["type", InclusiveGatewaySettings]
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/features/palette/Palette.js
  function Palette(eventBus, canvas) {
    var self = this;
    this._canvas = canvas;
    this.entries = [];
    this._init();
    eventBus.on(TOGGLE_MODE_EVENT, function(context) {
      var active = context.active;
      if (active) {
        classes(self.container).remove("hidden");
      } else {
        classes(self.container).add("hidden");
      }
    });
  }
  Palette.prototype._init = function() {
    this.container = domify('<div class="bts-palette hidden"></div>');
    this._canvas.getContainer().appendChild(this.container);
  };
  Palette.prototype.addEntry = function(entry, index2) {
    var childIndex = 0;
    this.entries.forEach(function(entry2) {
      if (index2 >= entry2.index) {
        childIndex++;
      }
    });
    this.container.insertBefore(entry, this.container.childNodes[childIndex]);
    this.entries.push({
      entry,
      index: index2
    });
  };
  Palette.$inject = ["eventBus", "canvas"];

  // ../../node_modules/bpmn-js-token-simulation/lib/features/palette/index.js
  var palette_default = {
    __init__: [
      "tokenSimulationPalette"
    ],
    tokenSimulationPalette: ["type", Palette]
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/base.js
  var base_default = {
    __depends__: [
      simulator_default,
      animation_default,
      colored_scopes_default,
      context_pads_default,
      simulation_state_default,
      show_scopes_default,
      log_default,
      element_support_default,
      pause_simulation_default,
      reset_simulation_default,
      token_count_default,
      set_animation_speed_default,
      exclusive_gateway_settings_default,
      neutral_element_colors_default,
      inclusive_gateway_settings_default,
      palette_default
    ]
  };

  // ../../node_modules/bpmn-js-token-simulation/lib/viewer.js
  var viewer_default2 = {
    __depends__: [
      base_default,
      viewer_default
    ]
  };

  // ../../token-sim-viewer-entry.mjs
  window.TokenSimulationViewerModule = viewer_default2;
})();
