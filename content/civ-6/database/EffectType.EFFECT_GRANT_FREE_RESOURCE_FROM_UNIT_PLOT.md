---
tags:
- EffectType
title: EFFECT_GRANT_FREE_RESOURCE_FROM_UNIT_PLOT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_FREE_RESOURCE_FROM_UNIT_PLOT
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="GREATPERSON_GRANT_PLOT_RESOURCE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_GRANT_PLOT_RESOURCE",
		"MODIFIER_PLAYER_GRANT_FREE_RESOURCE_FROM_UNIT_PLOT",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GREATPERSON_GRANT_PLOT_RESOURCE",
		"Amount",
		1
	);
	
```

