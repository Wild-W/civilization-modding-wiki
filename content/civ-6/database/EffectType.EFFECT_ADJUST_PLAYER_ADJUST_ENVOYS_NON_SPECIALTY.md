---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_ADJUST_ENVOYS_NON_SPECIALTY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_ADJUST_ENVOYS_NON_SPECIALTY
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Unknown`

## Samples

```SQL {title="TRAIT_FREE_ENVOY_WHEN_DISTRICT_MADE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_FREE_ENVOY_WHEN_DISTRICT_MADE",
		"MODIFIER_PLAYER_DISTRICT_ADJUST_PLAYER_ENVOYS_NON_SPECIALTY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_FREE_ENVOY_WHEN_DISTRICT_MADE",
		"Amount",
		1
	);
	
```

