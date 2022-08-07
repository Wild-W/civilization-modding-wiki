---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_IGNORE_ZOC
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_IGNORE_ZOC
>
> * Class: `UNITS`
> * Parameters:
>	* Ignore `Boolean`

## Samples

```SQL {title="IGNOREZOC_IGNORE_ZOC"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"IGNOREZOC_IGNORE_ZOC",
		"MODIFIER_PLAYER_UNIT_ADJUST_IGNORE_ZOC"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"IGNOREZOC_IGNORE_ZOC",
		"Ignore",
		1
	);
	
```

