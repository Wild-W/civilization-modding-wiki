---
tags:
- EffectType
title: EFFECT_UNIT_TRANSFER_CITY_AS_GIFT_AND_APPLY_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_UNIT_TRANSFER_CITY_AS_GIFT_AND_APPLY_MODIFIER
>
> * Class: `Unknown`
> * Parameters:
>	* ModifierId `Unknown`

## Samples

```SQL {title="GREATPERSON_CITY_STATE_ABSORB_EXPANSIONS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_CITY_STATE_ABSORB_EXPANSIONS",
		"MODIFIER_UNIT_ABSORB_CITY_STATE_AS_GIFT_AND_APPLY_MODIFIER",
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
		"GREATPERSON_CITY_STATE_ABSORB_EXPANSIONS",
		"ModifierId",
		"GREATPERSON_CITY_STATE_ABSORB_EXPANSIONS_LOYALTY_ATTACHMENT"
	);
	
```

