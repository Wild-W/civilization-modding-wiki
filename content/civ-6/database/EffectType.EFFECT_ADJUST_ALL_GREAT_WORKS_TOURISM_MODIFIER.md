---
tags:
- EffectType
title: EFFECT_ADJUST_ALL_GREAT_WORKS_TOURISM_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_ALL_GREAT_WORKS_TOURISM_MODIFIER
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="THEMED_TOURISM_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"THEMED_TOURISM_MODIFIER",
		"MODIFIER_PLAYER_ADJUST_THEMED_TOURISM"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"THEMED_TOURISM_MODIFIER",
		"Amount",
		100
	);
	
```

