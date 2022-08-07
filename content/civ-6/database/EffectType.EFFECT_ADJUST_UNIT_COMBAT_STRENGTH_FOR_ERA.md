---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_COMBAT_STRENGTH_FOR_ERA
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_COMBAT_STRENGTH_FOR_ERA
>
> * Class: `Unknown`
> * Parameters:
>	* AtomicEraAmount `Unknown`
>	* ClassicalEraAmount `Unknown`
>	* FutureEraAmount `Unknown`
>	* IndustrialEraAmount `Unknown`
>	* InformationEraAmount `Unknown`
>	* MedievalEraAmount `Unknown`
>	* ModernEraAmount `Unknown`
>	* RenaissanceEraAmount `Unknown`

## Samples
```SQL {title="MODIFIER_QUESTING_KNIGHT_ERA_STRENGTH"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"MODIFIER_QUESTING_KNIGHT_ERA_STRENGTH",
		"MODIFIER_ADJUST_COMBAT_STRENGTH_FOR_ERA",
		"QUESTING_KNIGHT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MODIFIER_QUESTING_KNIGHT_ERA_STRENGTH",
		"AtomicEraAmount",
		64
	),
	(
		"MODIFIER_QUESTING_KNIGHT_ERA_STRENGTH",
		"ClassicalEraAmount",
		12
	),
	(
		"MODIFIER_QUESTING_KNIGHT_ERA_STRENGTH",
		"FutureEraAmount",
		88
	),
	(
		"MODIFIER_QUESTING_KNIGHT_ERA_STRENGTH",
		"IndustrialEraAmount",
		40
	),
	(
		"MODIFIER_QUESTING_KNIGHT_ERA_STRENGTH",
		"InformationEraAmount",
		76
	),
	(
		"MODIFIER_QUESTING_KNIGHT_ERA_STRENGTH",
		"MedievalEraAmount",
		24
	),
	(
		"MODIFIER_QUESTING_KNIGHT_ERA_STRENGTH",
		"ModernEraAmount",
		52
	),
	(
		"MODIFIER_QUESTING_KNIGHT_ERA_STRENGTH",
		"RenaissanceEraAmount",
		32
	);
	
```

