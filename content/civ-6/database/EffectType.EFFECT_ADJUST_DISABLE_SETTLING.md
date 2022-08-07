---
tags:
- EffectType
title: EFFECT_ADJUST_DISABLE_SETTLING
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DISABLE_SETTLING
>
> * Class: `PLAYERS`
> * Parameters:
>	* Disabled `Boolean`

## Samples

```SQL {title="ISOLATIONISM_DISABLE_SETTLING"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ISOLATIONISM_DISABLE_SETTLING",
		"MODIFIER_PLAYER_DISABLE_SETTLING"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ISOLATIONISM_DISABLE_SETTLING",
		"Disabled",
		1
	);
	
```

