---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_PROPERTY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_PROPERTY
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Unknown`
>	* Key `Unknown`

## Samples

```SQL {title="POLICY_SAKDINA_PROJECT_POINTS_MULTIPLIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"POLICY_SAKDINA_PROJECT_POINTS_MULTIPLIER",
		"MODIFIER_PLAYER_ADJUST_PROPERTY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"POLICY_SAKDINA_PROJECT_POINTS_MULTIPLIER",
		"Amount",
		10
	),
	(
		"POLICY_SAKDINA_PROJECT_POINTS_MULTIPLIER",
		"Key",
		"PROJECT_POINTS_MULTIPLIER_PER_BUILDING"
	);
	
```

