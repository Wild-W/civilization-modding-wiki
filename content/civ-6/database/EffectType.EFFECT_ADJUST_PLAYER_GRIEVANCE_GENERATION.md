---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_GRIEVANCE_GENERATION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_GRIEVANCE_GENERATION
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="WC_RES_PLAYER_GRIEVANCES_BUFF"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"WC_RES_PLAYER_GRIEVANCES_BUFF",
		"MODIFIER_PLAYER_ADJUST_GRIEVANCE_MULTIPLIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"WC_RES_PLAYER_GRIEVANCES_BUFF",
		"Amount",
		100
	);
	
```

