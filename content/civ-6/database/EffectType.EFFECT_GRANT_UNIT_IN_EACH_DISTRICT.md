---
tags:
- EffectType
title: EFFECT_GRANT_UNIT_IN_EACH_DISTRICT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_UNIT_IN_EACH_DISTRICT
>
> * Class: `Unknown`
> * Parameters:
>	* IgnoreDefensible `Unknown`
>	* UniqueOverride `Unknown`
>	* UnitType `Unknown`

## Samples

```SQL {title="GREAT_PERSON_INDIVIDUAL_TUPAC_AMARU_ACTIVE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREAT_PERSON_INDIVIDUAL_TUPAC_AMARU_ACTIVE",
		"MODIFIER_GRANT_UNITS_IN_DISTRICTS",
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
		"GREAT_PERSON_INDIVIDUAL_TUPAC_AMARU_ACTIVE",
		"IgnoreDefensible",
		1
	),
	(
		"GREAT_PERSON_INDIVIDUAL_TUPAC_AMARU_ACTIVE",
		"UniqueOverride",
		1
	),
	(
		"GREAT_PERSON_INDIVIDUAL_TUPAC_AMARU_ACTIVE",
		"UnitType",
		"UNIT_MUSKETMAN"
	);
	
```

