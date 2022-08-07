---
tags:
- EffectType
title: EFFECT_ADJUST_FULL_ACCESS_ONE_STRATEGIC
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_FULL_ACCESS_ONE_STRATEGIC
>
> * Class: `PLAYERS`
> * Parameters:
>	* Access `Boolean`

## Samples
```SQL {title="RESOURCEMANAGEMENT_FULL_ACCESS_ONE_STRATEGIC"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"RESOURCEMANAGEMENT_FULL_ACCESS_ONE_STRATEGIC",
		"MODIFIER_PLAYER_ADJUST_FULL_ACCESS_ONE_STRATEGIC"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"RESOURCEMANAGEMENT_FULL_ACCESS_ONE_STRATEGIC",
		"Access",
		1
	);
	
```

