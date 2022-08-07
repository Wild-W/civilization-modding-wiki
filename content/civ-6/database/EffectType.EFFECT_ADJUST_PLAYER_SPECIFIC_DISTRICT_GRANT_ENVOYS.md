---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_SPECIFIC_DISTRICT_GRANT_ENVOYS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_SPECIFIC_DISTRICT_GRANT_ENVOYS
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Unknown`
>	* DistrictType `Unknown`

## Samples

```SQL {title="TRAIT_FREE_ENVOY_WHEN_DISTRICT_MADE_SPECIFIC"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_FREE_ENVOY_WHEN_DISTRICT_MADE_SPECIFIC",
		"MODIFIER_PLAYER_DISTRICT_ADJUST_SPECIFIC_DISTRICT_GRANT_ENVOYS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_FREE_ENVOY_WHEN_DISTRICT_MADE_SPECIFIC",
		"Amount",
		1
	),
	(
		"TRAIT_FREE_ENVOY_WHEN_DISTRICT_MADE_SPECIFIC",
		"DistrictType",
		"DISTRICT_GOVERNMENT"
	);
	
```

